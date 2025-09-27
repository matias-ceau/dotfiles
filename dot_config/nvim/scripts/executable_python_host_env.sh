#!/usr/bin/bash

NVIM_DATA=$XDG_DATA_HOME/nvim
PYTHON_NVIM_DIR=$NVIM_DATA/python-host-venv

mkdir -p $PYTHON_NVIM_DIR

[[ ! -d $PYTHON_NVIM_DIR ]] &&
uv \
    --directory "$NVIM_DATA" \
    venv python-host-venv \
    --seed &&
uv \
    --directory "$PYTHON_NVIM_DIR" \
    pip install pynvim openai google-generativeai pip neovim

