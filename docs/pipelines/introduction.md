# Pipelines
### Introduction
A common scenario in building a static site is the desire to apply the same process to hundreds, if not thousands, of files. To facilitate this, Skua offers pipelines. The idea with a pipeline is that a number of Skua classes can be stringed together and accessed as one unit in a `Pipeline` object.

### Basic guide
Skua offers some prebuilt pipelines. 
* `skua.pipelines.markdown_pipeline` – a pipeline for compiling markdown files to HTML. This is a function which returns a `Pipeline` instance. Usage: `markdown_pipeline(import_name, template_directory, config_object)`.
```python
from skua.pipelines import markdown_pipeline
from skua.preprocessors import Config
markdown_pipeline(__name__, 'src/templates', Config({'some_variables': 'here'}))
```
You can construct your own pipelines, this can be done using the `skua.pipelines.Pipeline` class. This class is initialized with a list of callable objects.  
```python
from skua.pipelines import Pipeline
from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.render import Templates
pipeline = Pipeline(Templates(__name__, 'src/templates'), MarkdownPreprocessor(Config({'some_variables': 'here'})))
```
### Pipeline process
1. Find files
2. Preprocess files (turn them into dictionaries)
3. Render files (produce HTML files)