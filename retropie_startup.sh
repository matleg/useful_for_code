#! /usr/bin/env bash
# RETROPIE PROFILE START

function getIPAddress() {
    local ip_route
    ip_route=$(ip -4 route get 8.8.8.8 2>/dev/null)
    if [[ -z "$ip_route" ]]; then
        ip_route=$(ip -6 route get 2001:4860:4860::8888 2>/dev/null)
    fi
    [[ -n "$ip_route" ]] && grep -oP "src \K[^\s]+" <<<"$ip_route"
}

function retropie_welcome() {
    local upSeconds="$(/usr/bin/cut -d. -f1 /proc/uptime)"
    local secs=$((upSeconds % 60))
    local mins=$((upSeconds / 60 % 60))
    local hours=$((upSeconds / 3600 % 24))
    local days=$((upSeconds / 86400))
    local UPTIME=$(printf "%d days, %02dh%02dm%02ds" "$days" "$hours" "$mins" "$secs")

    # calculate rough CPU and GPU temperatures:
    local cpuTempC
    local cpuTempF
    local gpuTempC
    local gpuTempF
    if [[ -f "/sys/class/thermal/thermal_zone0/temp" ]]; then
        cpuTempC=$(($(cat /sys/class/thermal/thermal_zone0/temp) / 1000)) && cpuTempF=$((cpuTempC * 9 / 5 + 32))
    fi

    if [[ -f "/opt/vc/bin/vcgencmd" ]]; then
        if gpuTempC=$(/opt/vc/bin/vcgencmd measure_temp); then
            gpuTempC=${gpuTempC:5:2}
            gpuTempF=$((gpuTempC * 9 / 5 + 32))
        else
            gpuTempC=""
        fi
    fi

    local df_out=()
    local line
    while read line; do
        df_out+=("$line")
    done < <(df -h /)

    local rst="$(tput sgr0)"
    local fgblk="${rst}$(tput setaf 0)" # Black - Regular
    local fgred="${rst}$(tput setaf 1)" # Red
    local fggrn="${rst}$(tput setaf 2)" # Green
    local fgylw="${rst}$(tput setaf 3)" # Yellow
    local fgblu="${rst}$(tput setaf 4)" # Blue
    local fgpur="${rst}$(tput setaf 5)" # Purple
    local fgcyn="${rst}$(tput setaf 6)" # Cyan
    local fgwht="${rst}$(tput setaf 7)" # White

    local bld="$(tput bold)"
    local bfgblk="${bld}$(tput setaf 0)"
    local bfgred="${bld}$(tput setaf 1)"
    local bfggrn="${bld}$(tput setaf 2)"
    local bfgylw="${bld}$(tput setaf 3)"
    local bfgblu="${bld}$(tput setaf 4)"
    local bfgpur="${bld}$(tput setaf 5)"
    local bfgcyn="${bld}$(tput setaf 6)"
    local bfgwht="${bld}$(tput setaf 7)"

    local logo=(
        "${fgred}   .***.   "
        "${fgred}   ***${bfgwht}*${fgred}*   "
        "${fgred}   \`***'   "
        "${bfgwht}    |*|    "
        "${bfgwht}    |*|    "
        "${bfgred}  ..${bfgwht}|*|${bfgred}..  "
        "${bfgred}.*** ${bfgwht}*${bfgred} ***."
        "${bfgred}*******${fggrn}@@${bfgred}**"
        "${fgred}\`*${bfgred}****${bfgylw}@@${bfgred}*${fgred}*'"
        "${fgred} \`*******'${fgrst} "
        "${fgred}   \`\"\"\"'${fgrst}   "
    )

    local out
    local i
    for i in "${!logo[@]}"; do
        out+="  ${logo[$i]}  "
        case "$i" in
        0)
            out+="${fggrn}$(date +"%A, %e %B %Y, %X")"
            ;;
        1)
            out+="${fggrn}$(uname -srmo)"
            ;;
        3)
            out+="${fgylw}${df_out[0]}"
            ;;
        4)
            out+="${fgwht}${df_out[1]}"
            ;;
        5)
            out+="${fgred}Uptime.............: ${UPTIME}"
            ;;
        6)
            out+="${fgred}Memory.............: $(grep MemFree /proc/meminfo | awk {'print $2'})kB (Free) / $(grep MemTotal /proc/meminfo | awk {'print $2'})kB (Total)"
            ;;
        7)
            out+="${fgred}Running Processes..: $(ps ax | wc -l | tr -d " ")"
            ;;
        8)
            out+="${fgred}IP Address.........: $(getIPAddress)"
            ;;
        9)
            out+="Temperature........: CPU: ${cpuTempC}°C/${cpuTempF}°F GPU: ${gpuTempC}°C/${gpuTempF}°F"
            ;;
        10)
            out+="${fgwht}The RetroPie Project, https://retropie.org.uk"
            ;;
        esac
        out+="${rst}\n"
    done
    echo -e "\n$out"
}

retropie_welcome
# RETROPIE PROFILE END
