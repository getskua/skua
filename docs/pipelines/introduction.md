# Pipelines
**Automated static site generation**

Skua's pipelines can be used to perform the same operation on a set of files many times. You can use prebuilt pipelines, or build your own.

### Prebuild (opinionated) pipelines
* `skua.files.markdown_pipeline` – a pipeline which takes markdown files and compiles them into HTML. Uses `HTMLPipeline`. Calling the `markdown_pipeline` function will return a `Pipeline` object which you can call using `Pipeline.compile_and_save_files()`
```python
from skua.pipelines import markdown_pipeline
from skua.preprocessors import Config
from pathlib import Path
pipeline = markdown_pipeline(Path('src'), Path('templates'), Config.from_file(Path('config.json'))) # This creates the pipeline
```

### Build your own pipelines