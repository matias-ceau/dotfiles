#! /usr/bin/env xonsh

#DOC#@RUN@=2024-06= "Play an album using cmus"
#+required+ cmus dmenu

import os
import random

temp_path = os.path.expanduser('~/.config/cmus/.temp.m3u') 

paths = $(cat .config/cmus/lib.pl).splitlines()
albums = list(set(['/'.join(i.split('/')[-3:-1]) for i in paths]))

fancy_dict = {k : (k.split('/')[0] ,  k.split('/')[-1]) for k in albums}
fancy_dict = {k : f"{i[:50]:>100}    \u2014    {j}" for k,(i,j) in fancy_dict.items()}
fancy_names = '\n'.join([v for v in fancy_dict.values()])

selected = $(echo @(fancy_names) | dmenu -i -l 300)

res_ = [f"{k}#{v}" for k,v in fancy_dict.items() if v in selected]
sel_path,sel_fancy = res_[0].split('#')

playlist_paths = [p+'\n' for p in paths if sel_path+'/' in p]

albums = [a for a in albums if sel_path+'/' not in a]
random.shuffle(albums)

rest = []
for a in albums[:10]:
    playlist_paths += [p+'\n' for p in paths if (a+'/') in p]
    print(playlist_paths[-1])

with open(temp_path, 'w') as f:
    f.writelines(playlist_paths)

cmus-remote -U
cmus-remote -C "view 4"
cmus-remote -C clear
cmus-remote -Q
cmus-remote -q @(temp_path)
cmus-remote -p
cmus-remote -n
