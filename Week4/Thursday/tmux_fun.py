import json
import time
import subprocess
import calendar

import datetime


def call_bash(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

if __name__ == "__main__":
    log_group_names = [
            1,2
    ]

    for log_group_name in range(4):
        command = f"tmux split-window asciiquarium | lolcat"
        call_bash(command)

    # alwaysoutofmana: ok so can you update the tmux commands
    # from inside vim without leaving the split?
    command = "tmux select-layout tiled"
    call_bash(command)
    command = f"tmux split-window asciiquarium | lolcat"
    call_bash(command)
