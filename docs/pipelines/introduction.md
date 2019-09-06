# Pipelines
**Automated static site generation**

Skua's pipelines can be used to perform the same operation on a set of files many times. You can use prebuilt pipelines, or build your own.

### Prebuild (opinionated) pipelines
* `skua.files.markdown_pipeline` – a pipeline which takes markdown files and compiles them into HTML. Uses `HTMLPipeline`.

### Build your own pipelines