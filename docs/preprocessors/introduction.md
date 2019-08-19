# Preprocessors
###### Turn files into dictionaries.
### Introduction
Skua's preprocessors allow you to convert static files into dictionaries, before you use a templating engine to convert these files into HTML files. 

If you imagine a static site generator to be like a compiler, dictionaries are Skua's internal language, to which everything must be converted before it can be rendered as an HTML file. 

### Basic usage
Skua preprocessors have to be given a `skua.preprocessors.Config` object before they can be used. The config object is a small class to which you pass a dictionary containing global variables (e.g. the website name, the author, Google Analytics configurations, etc.). This config object must be provided to all preprocessors you create. When each file is rendered, all the keys found in the static file's frontmatter are merged with the keys provided in the Config files. Keys in the config file overwrite keys provided in the frontmatter of files. 