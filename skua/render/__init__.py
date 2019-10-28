import glob
import os
import pathlib
import re
from multiprocessing import Queue, Process
from typing import Dict, Union

import jinja2


class Templates(object):
    def __init__(self):
        pass

    def render_template(self, template: str, **kwargs):
        """
        Render a template
        :param template: The name of the template
        :param kwargs: Key/value pairs to be passed to the template.
        :return:
        """
        return NotImplementedError("You need to override this class and implement this method before you can use it!")

    def __call__(self, template: str, **kwargs):
        return self.render_template(template, **kwargs)


class Jinja2Templates(Templates):
    def __init__(self, template_dir: Union[pathlib.Path, str], template_extension: str = 'html',
                 template_prefix: str = "skua_"):
        """
        A thin wrapper around jinja2's template environment.

        :param template_dir: The folder in which the templates are stored.

        :param template_extension: All files without this extension are ignored.

        :param template_prefix: All folders without this prefix are ignored. A sensible default is the name of your
        organisation.
        """
        if isinstance(template_dir, str):
            template_dir = pathlib.Path(template_dir)
        super(Jinja2Templates, self).__init__()
        if not template_dir.exists():
            raise NotADirectoryError(
                "The supplied template folder {} could not be found.".format(template_dir.resolve()))
        self.env = jinja2.Environment(
            # Use an absolute path.
            loader=jinja2.FileSystemLoader(str(template_dir.resolve()))
        )
        self.template_dir: pathlib.Path = template_dir

        template_dir_index = [template for template in
                              glob.glob(os.path.join(os.path.abspath(str(template_dir)), '**'), recursive=True) if
                              re.search(template_prefix, template) and os.path.splitext(os.path.split(template)[1])[
                                  1] == '.' + template_extension]

        self.templates: Dict = dict(
            [(os.path.splitext(os.path.split(str(template_file))[1])[0],
              self.env.get_template(os.path.relpath(template_file, str(template_dir)))) for
             template_file in template_dir_index])

    def render_template(self, template, **kwargs):
        """
        Takes a template and renders it as HTML.

        :param template: The template to be used. The template should be
        specified without the extension, e.g. to use the template `skua_blogpost.html` you would use `skua_blogpost`
        as the value for the argument `template.

        :param kwargs: Keyword arguments – these are all accessible to the jinja2 template enviroment.

        :return: The HTML output of the file.
        """
        try:
            return self.templates[template].render(**kwargs)
        except jinja2.exceptions.TemplateNotFound as e:
            print(
                "One of the templates that you are inheriting from or including cannot be found. Please ensure that "
                "you have specified the location of the template you are inheriting from as a path "
                "relative to {}".format(self.template_dir.resolve(), e))

    def __call__(self, template, **kwargs):
        """
        The __call__ method is implemented to allow this site to work with Pipelines. It does the exact same thing as
        `skua.render.Templates.render_template`.

        :param template: The template to be used. The template should be
        specified without the extension, e.g. to use the template `skua_blogpost.html` you would use `skua_blogpost`
        as the value for the argument `template.

        :param kwargs: Keyword arguments – these are all accessible to the jinja2 template environment.

        :return: The HTML output of the file.
        """
        return self.render_template(template, **kwargs)


def _render_file_jinja2(q, file_dictionary: dict, templates: dict, template_name: str):
    """

    :param file_dictionary:
    :param templates:
    :param template_name:
    :return:
    """
    q.put(templates[template_name].render(**file_dictionary))


def render_jinja2_parallel(dictionaries, template_prefix: str = 'skua_', template_extension: str = 'html',
                           template_dir: Union[pathlib.Path, str] = pathlib.Path('templates')):
    """

    :param dictionaries:
    :param template_prefix:
    :param template_extension:
    :param template_dir:
    :return:
    """
    if not isinstance(template_dir, pathlib.Path):
        template_dir = pathlib.Path(template_dir)

    template_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(str(template_dir.resolve())))

    template_dir_index = [template for template in
                          glob.glob(os.path.join(os.path.abspath(str(template_dir)), '**'), recursive=True) if
                          re.search(template_prefix, template) and os.path.splitext(os.path.split(template)[1])[
                              1] == '.' + template_extension]

    templates: Dict = dict(
        [(os.path.splitext(os.path.split(str(template_file))[1])[0],
          template_environment.get_template(os.path.relpath(template_file, str(template_dir)))) for
         template_file in template_dir_index])

    q = Queue()
    processes = [Process(target=_render_file_jinja2, args=(q, dictionary, templates, dictionary['template'])) for
                 dictionary in dictionaries]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    return [q.get() for _ in processes]
