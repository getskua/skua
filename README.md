# Skua
[![CircleCI](https://circleci.com/gh/teymour-aldridge/skua.svg?style=shield)](https://circleci.com/gh/teymour-aldridge/skua)
### A pythonic static site generator.
A static site generator written in Python. 
### Documentation
Skua's documentation is build using [MkDocs](https://mkdocs.org) and is hosted at [skua.netlify.com](https://skua.netlify.com).
### Command-line interface
Skua can be used from the command line (still under development). It takes every template it finds and places an HTML template in the chosen output folder. 
### Python scripting
Skua can be imported and used to create Python scripts, which allows for greater flexibility and custom site generation pipelines. 
### Versioning
Skua version numbers are in the format MAJOR.MINOR.PATCH.

* MAJOR: A major release will include breaking API changes and old code will need to be ported over to a new version. 
* MINOR: A minor release will be backwards compatible with all code on the same MAJOR version. It will release new functionality, but in a backwards compatible manner.
* PATCH: This is a small release to fix something within the latest MINOR version. It does not introduce new functionality.