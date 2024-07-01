#! /usr/bin/env xonsh

#DOC#@RUN@ "Create jupyter notebook and open it in chromium"

PROJECT_PATH = $HOME+"/projects"
empty_nb = """{\n  "cells": [],\n  "metadata": {},\n  "nbformat": 4,\n  "nbformat_minor": 2\n}"""

name = $(echo '' | dmenu)
if name != '\n':
    name = name.replace('\n','')
    name += '.ipynb'
    print(name)
    notebooks = $(ls @(PROJECT_PATH)).split('\n')
    print(notebooks)
    if name not in notebooks:
        path = f'{PROJECT_PATH}/{name}'
        with open(path, 'w') as f:
            f.write(empty_nb)
        jupyter-notebook --browser=chromium @(path)
    else:
        notify-send -u critical -c system "jupyter_new_notebook" "Named already exists!" -t 1999 
else:
    notify-send -u critical -c system "jupyter_new_notebook" "No named specified for the notebook!" -t 1999 

