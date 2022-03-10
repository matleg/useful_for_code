alias acl='sudo apt autoclean'
alias acs='sudo apt-cache search'
alias agar='sudo apt autoremove'
alias agi='sudo apt install'
alias agu='sudo apt update'
alias agup='sudo apt upgrade'
alias audio-hdmi='pacmd set-card-profile 0 output:hdmi-stereo+input:analog-stereo'
alias audio-laptop='pacmd set-card-profile 0 output:analog-stereo+input:analog-stereo'
alias c='clear'
alias cd..='cd ..'
alias cd-='cd -'
alias countfiles='find . -type f | wc -l'
alias cp='cp -r'
alias dir='dir --color=auto'
alias duu='du -sch .[!.]* * | sort -h'
alias e='exit'

function extract() {
    if [ -f $1 ]; then
        case $1 in
        *.tar.bz2) tar xvjf $1 ;;
        *.tar.gz) tar xvzf $1 ;;
        *.bz2) bunzip2 $1 ;;
        *.rar) unrar x $1 ;;
        *.gz) gunzip $1 ;;
        *.tar) tar xvf $1 ;;
        *.tbz2) tar xvjf $1 ;;
        *.tgz) tar xvzf $1 ;;
        *.zip) unzip $1 ;;
        *.Z) uncompress $1 ;;
        *.7z) 7z x $1 ;;
        *) echo "'$1' cannot be extracted via >extract<" ;;
        esac
    else
        echo "'$1' is not a valid file!"
    fi
}

alias ff='find . -name'
alias ffg='find . | grep'

function g { gedit $* & }

alias grep='grep --color=auto'
alias gw='gwenview'
alias h='history'
alias k='kill -9'
alias l='pwd; ls -lh --color'
alias ll='pwd; ls -lahrt --color'
alias ls='ls --color=auto'
alias lsd='l -d */'
alias lsp='l *.py'
alias maj='agu; agup; acl; agar'

# Create a tar.gz archive from given directory.
function maketar() { tar cvzf "${1%%/}.tar.gz" "${1%%/}/"; }
# Create a ZIP archive of a file or folder.
function makezip() { zip -r "${1%%/}.zip" "$1"; }
function mkcd() { mkdir "$@" && cd "$@"; }
function n { gedit $* & }
function na { nano $* & }
function noiptables() {
    sudo iptables -F
    sudo iptables -X
    sudo iptables -P INPUT ACCEPT
    sudo iptables -P OUTPUT ACCEPT
    sudo iptables -P FORWARD ACCEPT
}

alias nano='vim'
alias p='pwd'
alias pku='pkill -u mat'
alias psa='ps -ef | grep mat '
alias psg='ps -ef | grep '
alias rm='rm -rf'
alias running_services='systemctl list-units  --type=service  --state=running'
alias src='source ~/.bashrc'
alias sudo='sudo ' # for autocompletion (first word after ' ')
alias t='tail -f'
alias top='htop'
alias topu='htop -u mat'
alias v='vim'
alias ..='cd .. ; pwd'
alias ...='cd ../../; pwd'
alias ....='cd ../../../; pwd'
alias .....='cd ../../../../; pwd'
alias ......='cd ../../../../../; pwd'
