# Rendering
## Jinja2
[Jinja2](https://github.com/pallets/jinja2) is a popular templating language which is easy to use. To make it easier to get started with Jinja2, Skua provides a class called `Jinja2Templates` which provides an easy interface to render Jinja2 templates. 

To render files, `Jinja2Templates` offers a method `render_template` which takes the name of the template you want to use to render plus an unlimited number of keyword arguments which are made available to your Jinja2 templates as variables. Note that you can supply the template to use as a keyword argument as well. 

```python
from skua.render import Jinja2Templates
templates = Jinja2Templates('templates', template_extension='html', template_prefix='template_')
templates.render_template('template_blogpost', keyword='arguments')
```

### Parallel rendering
You may want to render lots of files in parallel. This is particularly useful in cases where you want to render lots of files quickly. Skua uses Python's `multiprocessing` module to get around the limitations imposed by the GIL (Global Interpreter Lock).

```python
from skua.render import render_jinja2_parallel
output_html = render_jinja2_parallel([{}, {}, {}, {}], template_prefix='skua_', template_extension='html', template_dir='templates')
# output html is a list of rendered html files – you then need to save these files somewhere.
```