# `skua.urls`
**Url manipulations**
### Introduction
Hyperlinks are an important part of any website. Skua has a few routines for handling them. 
### Converting paths into URLs
A path can be turned into a URL using `skua.urls.path2url`. This function needs to be provided the following parameters:

**args**
* `file` – a `pathlib.Path` object pointing to the file
* `site_url` – a string with the website URL

**kwargs**
* `output_directory`