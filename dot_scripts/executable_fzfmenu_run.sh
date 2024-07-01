#! /usr/bin/env bash

#DOC#@RUN@=2024-06= "Dmenu run replacement with fzf and a floating st terminal" 


dmenu_path | fzfmenu.sh | xargs -I {} bash -c "{}" &
