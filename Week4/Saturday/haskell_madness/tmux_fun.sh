#!/usr/bin/bash

# Create a new detached Tmux Session and name is make_workflow
tmux new-session -d -s make_workflow
 
# Split the window horizontally
tmux split-window -h

# Resize the pane to be 20 smaller
tmux resize-pane -R 20

# Select the initial pane
tmux select-pane -t 0

# Reattach to this session
tmux -2 attach-session -t make_workflow
