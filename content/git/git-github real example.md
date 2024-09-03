Movie Renamer Project
Merge only a specific commit from another branch

`git fetch origin <branch name>` fetch the another branch
`git checkout -B <branch> origin/branch` -B force creation of local branch from remote branch
`git log <branch>` see the commits and its hashes of that branch
`git checkout master`
`git cherry-pick <hash>` pick the commit from another branch and put it in the master branch, fix merge conflicts if needed

## FreeTube
Clone the repo
`git status` the correct one is in development
Add a new branch for your own changes `git checkour -c ryd`
`yarn` to install dependencies
```bash
git remote add patch https://github.com/ChunkyProgrammer/FreeTube
git fetch patch
git rebase patch/add-ryd
```
- resolve everything in the merge editor in VSCode
When FreeTube upstream changes
```bash
git fetch origin # fetch changes from remote repo
git rebase development
```
- merge changes if nessecary