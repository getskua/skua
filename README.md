# Skua
[![CircleCI](https://circleci.com/gh/teymour-aldridge/skua.svg?style=shield)](https://circleci.com/gh/teymour-aldridge/skua)
[![Netlify Status](https://api.netlify.com/api/v1/badges/b9b885cc-1a28-4640-be7e-d37b7b56703b/deploy-status)](https://app.netlify.com/sites/skua/deploys)

### A pythonic static site generator.
A static site generator written in Python. 
### Documentation
Skua's documentation is build using [MkDocs](https://mkdocs.org) and is hosted at [skua.netlify.com](https://skua.netlify.com).
### Command-line interface
Skua can be used from the command line (still under development). It takes every template it finds and places an HTML template in the chosen output folder. 
### Python scripting
Skua can be imported and used to create Python scripts, which allows for greater flexibility and custom site generation pipelines. 
### Versioning
Skua uses romantic versioning.
* MAJOR: A conceptually major change with (possible) breaking changes.
* MINOR: A conceptually minor change with (possible) breaking changes
* PATCH: Guaranteed not to cause any breaking changes. Used for minor changes, such as:
    * Bug fixes in the current version
    * Updates to algorithms which don't add extra dependencies.