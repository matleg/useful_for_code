#!/usr/bin/env bash

# from: https://unix.stackexchange.com/questions/62818/how-can-i-switch-between-different-audio-output-hardware-using-the-shell

#pacmd list-sinks
#pacmd list-cards
#alias audio-hdmi='pacmd set-card-profile 0 output:hdmi-stereo+input:analog-stereo'
#alias audio-laptop='pacmd set-card-profile 0 output:analog-stereo+input:analog-stereo'


CURRENT_PROFILE=$(pacmd list-cards | grep "active profile" | cut -d ' ' -f 3-)

if [ "$CURRENT_PROFILE" = "<output:hdmi-stereo>" ]; then
    pacmd set-card-profile 0 "output:analog-stereo+input:analog-stereo"
else 
    pacmd set-card-profile 0 "output:hdmi-stereo"
fi

