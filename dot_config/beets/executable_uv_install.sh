#!/usr/bin/bash

uv tool install https://github.com/beetbox/beets.git -p 3.13
cd `uv tool dir` || exit
cd beets || exit
uv pip install pyacoustid python3-discogs-client pylast requests
