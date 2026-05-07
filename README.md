Tanuki: Collection and Rendering of Git Repositories
====================================================

_Tanuki_ is a program that, given a list of URLs to Git repositories, will
fetch those repos to keep local copies of them and render their files to
HTML files that can be viewed in a web browser. (Typically, these will be
served by a web server, so this can be considered a static web site
builder.)

`tanuki` is given one argument, the directory containing configuration
data, the repos, and into which to place the rendered output. Under this
directory will be:

* `repo.list`: Each line is a path under `repo/` followed by one or more
  space-separated URLs suitable for `git fetch`. (Spaces within paths or
  URLs may be escaped with `\`.) `tanuki` never updates this file, but it's
  expected that external programs or humans will do so.

* `repo/`: Bare Git repositories  in directories named for the paths in
  `repo.list`. (These always end in `.git`; it's added if not supplied to
  make clear that these are bare repos.) These may have multiple remotes
  ("origins"), but any single repo is intended to be the nominal sum of all
  remotes.

* `view/`: Directories named as under `repo/` but with rendered views of
  the repository/commit contents. It's assumed that given path `x/`,
  `x/index.html` will be rendered. (See more below.)

#### Filename Linking

* Fetching `view/` will redirect to or return `view/index.html`, which will
  return a list of all repos.
* Fetching `view/REPO/` will redirect to or return `view/REPO/index.html`,
  which will be the start point for browsing the repo at the most recent
  (`HEAD`) commit from (XXX which source?)


Testing
-------

Running the `Test` script at the top level will test the system. Give `-h`
for more help.Use


TODO
----
