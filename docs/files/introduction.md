# Files
*A set of routines to help with the compilation of static sites.*
### `FindFiles` classes
* `FindFilesByExtension` – locates all the files within a directory (and subdirectories) with a specified extension (by default `md`).
### Git routines
!!! warning
    **Warning: This is untested code! Configuring a git repository inside a git repository is tricky, so the code remains untested.**

Many static sites make use of git to run continuous deployment (where commits to a git repository prompt updates to a website). To prevent unnecessary recompilations of files (which costs computing power) Skua provides a small `Git` object which detects changed markdown files within a repository, which means that there is no need to recompile already compiled files. 