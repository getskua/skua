# Render
*Turn static files into HTML.*
### Introduction
Skua provides a `skua.templates.Templates` class – a small wrapper around a Jinja2 environment. The `Templates` object needs to be initialised with the template folder – provided as a `pathlib.Path`. Jinja2 templates need to be prefixed with the user-specified prefix (by default "skua_" - specified in the keyword argument `template_prefix`) and have the user-specified extension (by defualt `html` – specified in the keyword argument `template_extension`)
```python
from pathlib import Path
from skua.render import Templates
templates = Templates(Path('src/templates'), template_prefix='template_', template_extension='html')
```