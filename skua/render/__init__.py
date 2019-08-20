import glob
import os
import re
from typing import Dict

import jinja2


class Templates(object):
    def __init__(self, import_name, template_dir: str, template_extension: str = 'html',
                 template_prefix: str = "skua_"):
        """
        Stores jinja2 templates. Please note that templates need to be unique.
        :param import_name: Usually `__name__` (a builtin variable)
        :param template_dir: The folder in which the templates can be found.
        :param template_extension: All files without this extension are ignored.
        """
        if not os.path.isdir(template_dir):
            raise LookupError("The template folder cannot be found.")
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir)
        )
        template_dir_index = [template for template in
                              glob.glob(os.path.join(os.path.abspath(template_dir), '**'), recursive=True) if
                              re.search(template_prefix, template) and os.path.splitext(os.path.split(template)[1])[
                                  1] == '.' + template_extension]

        self.templates: Dict = dict(
            [(os.path.splitext(os.path.split(str(template_file))[1])[0],
              self.env.get_template(os.path.relpath(template_file, template_dir))) for
             template_file in template_dir_index])

    def render_template(self, template, **kwargs):
        return self.templates[template].render(**kwargs)
