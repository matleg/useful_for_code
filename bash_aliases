 
alias acl='sudo apt autoclean'
alias acs='sudo apt-cache search'
alias agar='sudo apt autoremove'
alias agi='sudo apt install'
alias agu='sudo apt update'
alias agup='sudo apt upgrade'
alias c='clear'
alias cd..='cd ..'
alias cd-='cd -'
alias countfiles='find . -type f | wc -l'
alias cp='cp -r'
alias dir='dir --color=auto'
alias duu='du -sch .[!.]* * | sort -h'
alias e='exit'
alias egrep='egrep --color=auto'
alias ff='find . -name'
alias fgrep='fgrep --color=auto'

function g { gedit $* & }

alias grep='grep --color=auto'
alias gw='gwenview'
alias h='history'
alias k='kill -9'
alias l='pwd; ls -lh --color'
alias ll='pwd; ls -lha --color'
alias ls='ls --color=auto'
alias lsd='l -d */'
alias lsp='l *.py'
alias maj='agu; agup; acl; agar'

function mkcd() { mkdir "$@" && cd "$@"; }
function n { pluma $* & }
function na { nano $* & }

alias p='pwd'
alias pku='pkill -u mat'
alias psa='ps -ef | grep mat '
alias psg='ps -ef | grep '
alias rm='rm -rf'
alias src='source ~/.bashrc'
alias sudo='sudo '  # for autocompletion (first word after ' ')
alias t='tail -f'
alias top='htop'
alias topu='htop -u mat'
alias vdir='vdir --color=auto'
alias v='vim'
alias ..='cd .. ; pwd'
alias ...='cd ../../; pwd'
alias ....='cd ../../../; pwd'
alias .....='cd ../../../../; pwd'
alias ......='cd ../../../../../; pwd'
