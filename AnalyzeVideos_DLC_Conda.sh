#!/bin/bash

#initialize anaconda:
__conda_setup="$('/home/smith/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/smith/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/smith/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/smith/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
conda init bash
#activate the environment and run script:
conda activate dlc
python3 /d1/software/PiRATeMC/AnalyzeVideos_DLC.py
exit
