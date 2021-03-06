# Files
*A set of routines to help with the compilation of static sites.*
### `FindFiles` classes
FindFiles classes are classes which, when called, return a list of files. These can be used in pipelines to find files to be compiled.
 
* `FindFilesByExtension` – locates all the files within a directory (and subdirectories) with a specified extension (by default `md`).
### `skua.files.generate_index`
Returns a generator object of dictionaries containing the frontmatter, contents and a `pathlib.Path` object (which points to the file's location) of all the files in a folder. To search in subdirectories as well you can specify that the keyword argument `recursive=True`.
### Git routines
!!! warning
    **Warning: This is untested code! Configuring a git repository inside a git repository is tricky, so the code remains untested.**

Many static sites make use of git to run continuous deployment (where commits to a git repository prompt updates to a website). To prevent unnecessary recompilations of files (which costs computing power) Skua provides a small `Git` object which detects changed markdown files within a repository, which means that there is no need to recompile already compiled files. 