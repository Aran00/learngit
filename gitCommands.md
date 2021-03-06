01 	git config --global user.name "Aran"
02 	git config --global user.email "yuran00@gmail.com"
03 	git init
04 	git add readme.txt
    	Add changes to stage
05 	git commit -m "wrote a readme file"
 	  	Commit the changes in stage to master
06 	git status		
07 	git diff readme.txt
08 	git log
   	git log --pretty=oneline
	git log -n 1    git log -1 只输出一条log（最近的）
09 	git reset --hard HEAD^
   		Back to the last revision
   		Now the lastest commit would be invisible in git log results
10  	git reset --hard 5b9c728f
    	Commit id should be known at first, need not to be complete
11 	git reflog
	    Show all the change logs

Working Directory, Repository(.git directory), stage, master

12 	git checkout -- readme.txt
    	Revert the file to the status of last git commit/add.
13 	git reset HEAD readme.txt
 	  	Revoke the changes in stage, and put them to working directory
场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，⽤命令git checkout -- file。
场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD file，就回到了场景1，第⼆步按场景1操作。
场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

14	git rm test.txt 
    	If you have git add/rm, and want to recover the stage, use [git reset HEAD]; If you want the working directory and 
stage all revert to the last commit, use [git reset --hard HEAD]

The remote repository
generate a pair of RSA key to relate pub key with your commit

15	git remote add origin https://github.com/Aran00/learngit.git
    	git remote add origin git@github.com:Aran00/learngit.git
	git remote add [shortname] [url]
    	Relate current directory with remote repository
	git remote set [origin-name] [url]
		Reset some remote url

16 	git remote -v
		See the remote repositories

17  git push [-u] origin master/dev
		push local branch to remote repository
    	-u is used when pushing content at the first time

18  git clone git@github.com:Aran00/learngit.git
	git clone https://username:password@github.com/username/repository.git
	    Would add learngit folder under current directory

19 	git pull
		Merge the remote origin repository's change to current working copy(direct update)

20 	git checkout -b dev
		is equal to 2 commands:
	git branch dev			# Create a branch "dev"
	git checkout dev

	git checkout master
		Switch to branch "master"

	git checkout -b dev origin/dev
		Create remote origin dev branch to local repository

21	git branch
		list all the branches

22 	git merge dev
		merge dev branch to master

23 	git branch -d dev
		delete dev branch
	git branch -D feature-1
		delete a branch forcefully
	git branch -m <oldname> <newname>
		rename a branch
	git push origin --delete device-manage
		delete a remote branch
	Git鼓励大量使用分支：
	查看分支：git branch
	创建分支：git branch name
	切换分支：git checkout name
	创建+切换分支：git checkout -b name
	合并某分支到当前分支：git merge name
	删除分支：git branch -d name

24	git log --graph --pretty=oneline --abbrev-commit
	View the merge(conflict) situations of all branches. The last option is used for shortage the version id.

25	git merge --no-ff -m "merge with no-ff" dev
	Use --no-ff means create a new commit when merging the branches(See michael's graphs), and the log viewer can see merging history by it

26 	git stash
		Save working copy and index state
	git stash list
		View all the stash contents
	git stash pop 
		Recover the stash content to working directory, and delete stash content	
	git stash apply stash@{0}
		Recover some stash to working directory, not delete stash content
	git stash drop stash@{0}
		delete some stash

27	git branch --set-upstream-to=origin/dev dev
Branch dev set up to track remote branch dev from origin.
因此，多人协作的工作模式通常是这样：
1. 首先，可以试图用git push origin branch-name推送自己的修改；
2. 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功！

28	git tag [tagName] [versionId]
	git tag
		list all tags(sort by alphabets)
	git show [tagName]
	git tag -a [tagName] -m "version 0.1 released" [versionId]
	git tag -d v0.1

29 	git push origin v1.0
		Push some tag to remote
	git push origin --tags
		Push all tags to remote
	git tag -d v1.0
	git push origin :refs/tags/v1.0
命令git push origin tagname可以推送一个本地标签；
命令git push origin --tags可以推送全部未推送过的本地标签；
命令git tag -d tagname可以删除一个本地标签；
命令git push origin :refs/tags/tagname可以删除一个远程标签。

30 	如何参与一个开源项目呢比如人气极高的bootstrap项目，这是一个非常强大的CSS框架，你可以访问它的项目主页https://github.com/twbs/bootstrap,点“Fork”就在自己的账号下克隆了一个bootstrap仓库，然后，从自己的账号下clone：
git clone git@github.com:michaelliao/bootstrap.git
一定要从自己的账号下clone仓库，这样你才能推送修改。如果从bootstrap的作者的仓库地址git@github.com:twbs/bootstrap.git克隆，因为没有权限，你将不能推送修改。

31	Ignore special files
	Edit .gitignore file to do it. Content can be like this:
# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build

	git config --global core.excludesfile ~/.gitignore 
Ignore some files globally

32	Configure alias
$ git config --global alias.st status
$ git config --global alias.co checkout
$ git config --global alias.ci commit
$ git config --global alias.br branch

33	list all files’ revision ids
git ls-tree -r HEAD
git ls-tree --abbrev -l -r 52d0f

34  	About git objects:
https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

35 See branch to which origin-branch
$ git branch -vv
  main   aaf02f0 [main/master: ahead 25] Some other commit
* master add0a03 [jdsumsion/master] Some commit

36 Compare the local committed content with remote
	git log origin/master..HEAD

37 When merge confict
    git checkout --ours index.html
	git checkout --theirs _layouts/default.html

38 Check which branches have been merged to another
	git branch --merged develop-Tech

39 If you want to revert changes made to your working copy, do this:
	git checkout .
	
	If you want to revert changes made to the index (i.e., that you have added), do this. Warning this will reset all of your unpushed commits to master!:
	git reset

	If you want to revert a change that you have committed, do this:
	git revert ...
	
	If you want to remove untracked files (e.g., new files, generated files):
	git clean -f
	
	Or untracked directories (e.g., new or automatically generated directories):
	git clean -fd
