clean: rm -rf dist/*
docs: mkdocs build
package: python setup.py sdist; python setup.py bdist_wheel