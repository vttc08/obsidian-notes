Reset
`git reset 'hash'` reset the head to a previous commit
	- nothing is done to the code yet, unless using `git restore --staged` && `git restore`
	- if accidently reset, use `git reset 'HEAD@{1}'` to revert the progress to the previous git change

Rebase
- squash, take the current commit and combine it with previous commit
- fixup, like squash, combine the commit but not use the commit message

 ![](assets/Pasted%20image%2020231216234558.png)

This combine the license term commit and readme commit to a single commit and keep the commit message of "9e56146".

**Branches**
use `git switch -c` or `git checkout -b`
- now we can work on the features of new branch
Once the feature is done, to merge it with master
```
git switch master
git merge <branch-name>
```
- delete the branch `git branch -d <name>`
![](assets/Pasted%20image%2020231217000344.png)

**Merge Conflicts**
It can happen when two people are working on the different feature but both are changing the same file causing a conflict.
- in a new branch I added some codes
- then in the main branch I added some conflicting code
- upon `git merge newfeature`, the merge failed due to conflicts
![](assets/Pasted%20image%2020231217001341.png)
- there is option to accept current, incoming, ignore both or accept combination
![](assets/Pasted%20image%2020231217001713.png)
![](assets/Pasted%20image%2020231217001831.png)
this is an example of accept combination

Stash - quickly save the unstaged changed to a stash to add for later
- `git stash` to create a stash
- `git stash list`
- `git stash apply 0` to apply the stash to the current code
