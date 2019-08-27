import glob
import os
import pathlib
import re
from typing import Dict

import jinja2


class Templates(object):
    def __init__(self, template_dir: pathlib.Path, template_extension: str = 'html',
                 template_prefix: str = "skua_"):
        """
        Stores jinja2 templates. Please note that templates need to be unique.
        :param template_dir: The folder in which the templates can be found.
        :param template_extension: All files without this extension are ignored.
        """
        if not template_dir.exists():
            raise LookupError("The template folder cannot be found.")
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(str(template_dir))
        )
        template_dir_index = [template for template in
                              glob.glob(os.path.join(os.path.abspath(str(template_dir)), '**'), recursive=True) if
                              re.search(template_prefix, template) and os.path.splitext(os.path.split(template)[1])[
                                  1] == '.' + template_extension]

        self.templates: Dict = dict(
            [(os.path.splitext(os.path.split(str(template_file))[1])[0],
              self.env.get_template(os.path.relpath(template_file, str(template_dir)))) for
             template_file in template_dir_index])

    def render_template(self, template, **kwargs):
        return self.templates[template].render(**kwargs)

    def __call__(self, template, **kwargs):
        """
        The __call__ method is implemented to allow this site to work with Pipelines.
        :param template:
        :param kwargs:
        :return:
        """
        return self.render_template(template, **kwargs)
