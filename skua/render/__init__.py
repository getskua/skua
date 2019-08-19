import os
from pathlib import Path
from typing import Dict

import jinja2


class Templates(object):
    def __init__(self, import_name, template_dir: str, template_extension='html'):
        """
        Stores jinja2 templates. Please note that templates need to be unique.
        :param import_name: Usually `__name__` (a builtin variable)
        :param template_dir: The folder in which the templates can be found.
        :param template_extension: All files without this extension are ignored.
        """
        if not os.path.isdir(template_dir):
            raise LookupError("Could not find that directory.")
        self.path = Path()
        self.env = jinja2.Environment(
            loader=jinja2.PackageLoader(import_name, template_dir)
        )
        self.template_dir_index = self.path.glob(
            os.path.join(os.path.abspath(template_dir), '**', '*.' + template_extension))
        self.templates: Dict = list(
            [(os.path.splitext(os.path.split(str(template_file))[1])[0], self.env.get_template(template_file)) for
             template_file in self.template_dir_index])

    def render_template(self, template, file_dict):
        self.templates[template].render_template(**file_dict)
