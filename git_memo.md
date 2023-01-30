## working with detached HEAD

```sh
git checkout commit_ID
git commit
git commit
....
git branch tmp
git checkout master
git merge tmp
```

or directly:

```sh
git checkout -b tmp commit_ID
git commit
git commit
....
git checkout master
git merge tmp
```

## delete distant branches

```sh
git push [distant_name] [local_branch]:[distant_branch]

# if local_branch is empty, it means distant_branch is deleted, simply!
# ex:

git push origin  :[distant_branch]

# origin: default name for remote repository
# possible to work with several remote repositories hosted in different places
```

## reset & go back

```sh
git reset --hard HEAD^ : cancel last commit (the only one possible)
git reset file     or     git reset commit_ID : files remain modified
git show commit_ID:/path/to/file > file.old  : export previous version of file
```

## rebase

git rebase ONLY if nobody is looking at the branch! Otherwise, git revert or something else

## configure local and distant repositories

from: https://gist.github.com/jpierson/b6c0815e9dd7078f6b8cc3cb9076ddf4

```sh
git clone git@github...some-repo.git
```

rename your origin remote to upstream

```sh
git remote rename origin upstream
```

Add a new origin

```sh
git remote add origin git@github...my-fork
```

Fetch from new origin

```sh
git fetch origin
```

Set origin master

```sh
git branch --set-upstream-to origin/master master
```

Push to fork

```sh
git push origin
```

##

##

##

##

##
