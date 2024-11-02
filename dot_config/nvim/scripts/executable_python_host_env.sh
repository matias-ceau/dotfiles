#!/usr/bin/bash

NVIM_DATA=$XDG_DATA_HOME/nvim
PYTHON_NVIM=$NVIM_DATA/python-host-venv

[[ ! -d $PYTHON_NVIM ]] &&
uv \
    --directory "$NVIM_DATA" \
    venv python-host-venv \
    --seed &&
uv \
    --directory "$PYTHON_NVIM" \
    pip install pynvim openai google-generativeai pip neovim

