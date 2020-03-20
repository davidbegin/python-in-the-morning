#!/usr/bin/bash

tmux new-session -d -s beginbot
 
tmux new-window -t beginbot:1 -n 'asciiquarium' 'asciiquarium'
tmux new-window -t beginbot:2 -n 'cmatrix' 'cmatrix'
# tmux new-window -t beginbot:3 -n 'Server3' 'asciiquarium | lolcat'
# tmux new-window -t beginbot:4 -n 'Server4' 'asciiquarium | lolcat'
# tmux new-window -t beginbot:5 -n 'Server5' 'asciiquarium | lolcat'
 
tmux select-window -t beginbot:1
tmux split-window -h
tmux send-keys "make" C-m

# # tmux select-pane -t 0

tmux select-window -t beginbot:0
tmux -2 attach-session -t beginbot

# SESSION=$USER

# # tmux new
# tmux new-session -s $SESSION


# # # Setup a window for running Make
# # tmux new-window -t $SESSION:1 -n 'Makefile'
# # tmux split-window -h
# # tmux select-pane -t 0
# tmux send-keys "make" -s $SESSION C-m
# tmux send-keys "sleep 10" -s $SESSION C-m

# # tmux select-pane -t 1
# # echo "Pane1"
# # sleep 10
# # # command = "tmux select-layout tiled"
