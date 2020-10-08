
# eval "$(pyenv init -)"
# source ~/.nvm/nvm.sh
source ~/.git-prompt.sh


GIT_PS1_SHOWDIRTYSTATE=true
GIT_PS1_SHOWUNTRACKEDFILES=true

PS1='\[\e[30;43;1m\]Linux: \W \$ \[\e[1;93;45m\]►\[\e[1;97;45m\]$(__git_ps1 "%s") \[\e[1;35;40m\]►\[\e[0m\]'

alias ls='ls -AFG'
alias tree='tree -aC'
alias brew="env PATH=${PATH/\/Users\/lab\.\/\.pyenv\/shims:/} brew"

function git-branch-state(){
    branchState=$(__git_ps1 "%s")
    echo $branchState | awk '{sub(" .*", "");print $0;}'
}

alias git-addcancel='git reset HEAD'
alias git-comcancel='git reset --soft HEAD^'
alias git-ignore='git rm -r --cached'

git-comish(){
    if [ $# != 1 ];then
        printf "\e[33m%s\n\e[m" "incorrect number of arguments"
        return
    fi

    if [ "$(git remote -v)" ] ; then
        git commit -m "$1" && git push origin $(git-branch-state)
    else
        printf "\e[33m%s\n\e[m" "please set remote repository"
    fi
}
git-adomish(){
    if [ $# != 1 ];then
        printf "\e[33m%s\n\e[m" "incorrect number of arguments"
        return
    fi

    if [ "$(git remote -v)" ] ; then
        git add --all && git commit -m "$1" && git push origin $(git-branch-state)
    else
        printf "\e[33m%s\n\e[m" "please set remote repository"
    fi
}

git-mergesh(){
    if [ $# != 1 ];then
        printf "\e[33m%s\n\e[m" "incorrect number of arguments"
        return
    fi
    git merge --no-ff "$1" -m "[merge] with $1" && git push origin $(git-branch-state)
}

git-checkmerge(){
    current_branch=$(git-branch-state)
    if [ "$current_branch" = "$1" ];then
        printf "\e[33m%s\n\e[m" "can't merge same branch"
    else
        git checkout $1 && git merge $current_branch
    fi
}



git-init(){
    if [ $# != 1 ];then
        printf "\e[33m%s\n\e[m" "incorrect number of arguments"
        return
    fi
    git init
    git remote add origin "$1"
    git remote -v
    git commit --allow-empty -m "[empty]"
    git push origin master
}

git-log(){
    command git log --oneline --graph --all
}



fnum(){
    ls -lARU "$1" | grep -c '^-'
}
