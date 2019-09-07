# `skua.urls`
**Url manipulations**
### Introduction
Skua has some routines to handle URLs. 
### Turning relative links into URLs. 
A path can be turned into a URL using `skua.urls.path2url`. This function requires that all of the urls in your project begin from the source directory of your static site. 

**args**

* `file` – a `pathlib.Path` object pointing to the file
* `site_url` – a string with the website URL

**kwargs**

* `source_directory` – where all the source files are stored. 