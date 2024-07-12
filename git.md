### go back to selected commit in our local enviroment.
	$ git checkout <commit-id> . On top of your current status, tranform the files to return to commitid
	$ git checkout <commit-id>

### Check if pull needed
`$ git remote update` bring your remote refs up to date. and do:
	1. `git status -uno` will tell you whether the branch you are tracking is ahead, behind or has diverged. If it says nothing, the local and remote are the same.
	2. `git show-branch *master` will show you the commits in all of the branches whose names end in 'master' (eg master and origin/master).

### Save un-commited changes
	$ git stash save "add style to our site"

### Stash list
	$ git stash list

### Apply Stach
	$ git stash apply stash@{0}

### Create patch from diffs
`git diff > my_custom_patch_file.patch`

### Apply patch
`git apply patch_file.patch`

### Difference between branches
`git diff branch1..branch2`

### Difference between 2 files of different branch
`git difftool branch1:path/to/file branch2:path/to/file`