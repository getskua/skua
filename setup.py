import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skua",
    version="0.0.1",
    author="Teymour Aldridge",
    author_email="teymour.aldridge@icloud.com",
    description="A static site generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teymour-aldridge/skua",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
