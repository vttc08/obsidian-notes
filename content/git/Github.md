First create a github repository then add the remote
`git remote add origin <url of repo>`
To push a branch to the repo
`git push -u origin <branch name>`
To push all the branches
`git push --all`
In the case there are errors, use the following [github post](https://github.com/nss-evening-cohort-13/student-help/issues/76) to fix
After a rebase, force push to github to avoid errors
`git push origin +branch`

`git clone` get files from github into local harddrive
`git fetch` get the git data from github to local
`git pull` update the files from github with the commits
On github, there is options to set website, description and tags.

**Branches**
The default branch in github is `master`, any new branches through Github pull request would be based on master branch. This can be changed.
- go to Settings -> General -> Default Branch

**Issues** are todo items for yourself and from others and can be assigned to others
**Actions** run tests, automations
**Projects** 
**Wiki** documentation site 
- these are separate repo for the main repo that can be cloned
**Security**
**Insights** allow insights on who is contributing
**Github Page** host static site from github repo
- can use jekyll to convert md file into website

**Github Flow**
We have a main branch, and everytime need change, make a feature branch and commit to that branch. When it's time to merge into main branch, make a pull request. Once approved, it will be merged and to resolve any conflicts, then the feature branch can be deleted.

**Markdown**
```md
# Headline
# (up to 6 #)
> quotation
*italic* **bold**
*** -> make a line spacer
~~strikethrough~~
- item 1
- item 2
* item 3
	- with indent
[Link Text](link_url)
![Image reference](image_url)
`insert code here` - use 3 quotation for longer code
Footnote[^1]
[^1] references text/url
| Table | Table 2 | Table 3 |
| ----- | ------- | ------- |
| text  | text 2  | text 3  |
:--: centered, --: right aligh, default is left

```
**Repo Files**
Readme file - what the repo does, the homepage
-  in the main folder, `roots, docs, .github`
License
- has to be in the root folder
CODE_OF_CONDUCT.md - how should people use the repo
SECURITY.md - security policy
CONTRIBUTING.md - how to contribute
SUPPORT.md - how to get support for project

**Github Organization**
Contributors - Settings > Collaborators
Issues -> Create issue tab
- you can assign multiple users or use a milestone to an issue
Project - create checklist of issues for repos
Milestone - 



**Discussion** - discussion other than code issues, discussion can be pinned
**Gists** - share code snippets `gist.new`