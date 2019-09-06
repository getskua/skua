# Preprocessors
###### Turn files into dictionaries.
### Introduction
Skua's preprocessors allow you to convert static files into dictionaries, before you use a templating engine to convert these files into HTML files. 

If you imagine a static site generator to be like a compiler, dictionaries are Skua's internal language, to which everything must be converted before it can be rendered as an HTML file. 

### Config objects
Often websites have global variables such as the site name, site author, branding, etc. Instead of writing these global variables into every file, it is easier to just specify them once. Skua allows you to pass a `skua.preprocessors.Config` object to preprocessors. The `Config` class needs to be initialized with a dictionary in the format `{"variable_name":"value"}`. All keys in the dictionary will be available to all templates. 

`Config` objects can also be initialized using the `from_file` class method. The file specified must be a JSON file. 
```python
from pathlib import Path
from skua.preprocessors import Config
config = Config.from_file(Path('file_path.json'))
```

#### Useful keys you might want to set
* `template` – if you want to render all pages using the same template, then you can specify it in the config object. Note that template names should be specified without the extension, so if the template you want to use is called `skua_blogpost.html` you'd write `skua_blogpost`. Note that currently keys from `Config` objects override keys specified in frontmatter (although this will most likely change).
* `site_name` – this is the name of the site. If you are writing your own templates, then you can use a different variable name for this variable. By convention, this variable name is used. 
#### Example code
* Using the MarkdownPreprocessor
```python
from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.preprocessors import Config
md_preprocessor = MarkdownPreprocessor(Config({'site_name': 'My New Website!'}))
```