#!/usr/bin/bash

uv tool install beets -p 3.12
cd `uv tool dir` || exit
cd beets || exit
uv pip install pyacoustid python3-discogs-client pylast requests