# source : https://www.tldp.org/LDP/abs/html/sample-bashrc.html

# add to path
PATH="/home/mat/.local/bin:$PATH"

# dynamic libraries
export LD_LIBRARY_PATH="/home/mat/.local/lib/:$LD_LIBRARY_PATH"

# prompt for git
function color_my_prompt {
    local __user_and_host="\[\033[01;32m\]\u@\h"
    local __cur_location="\[\033[01;34m\]\w"
    local __git_branch_color="\[\033[31m\]"
    local __git_branch='`git branch 2> /dev/null | grep -e ^* | sed -E  s/^\\\\\*\ \(.+\)$/\(\\\\\1\)\ /`'
    local __prompt_tail="\[\033[35m\]$"
    local __last_color="\[\033[00m\]"
    export PS1="$__user_and_host $__cur_location $__git_branch_color$__git_branch$__prompt_tail$__last_color "
}

if [ -f ~/.git-prompt.sh ]; then
    . ~/.git-prompt.sh
    color_my_prompt
fi

# Key bindings, up/down arrow searches through history
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'
bind '"\eOA": history-search-backward'
bind '"\eOB": history-search-forward'

# Store multi-line commands in one history entry:
shopt -s cmdhist
HISTCONTROL="$HISTCONTROL:erasedups"

# timeout and display for ssh connexions
export TMOUT=0
if [ ! $DISPLAY ] ; then
    if [ "$SSH_CLIENT" ] ; then
        export DISPLAY=`echo $SSH_CLIENT|cut -f1 -d\ `:0.0
    fi
fi


