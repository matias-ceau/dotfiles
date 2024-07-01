#! /usr/bin/python3

#DOC#@CLI@$deprecated$ "Old script that changes album metadata"

import pandas as pd
import os
import subprocess

PATH = os.path.expanduser('~/notes/')
GENRE_NB = 5

# DETECT ALBUMS THAT HAVE BEEN LISTENED TO
print('Detecting albums you listened to...')
id_list = []
for i in [i for i in os.listdir(PATH) if (i[-3:]=='.md' and 'albums_to_listen' in i)]:
    p = PATH+i
    with open(p,'r') as f:
        lines = f.readlines()
        for line in lines:
            if '[' in line and ']' in line:
                if '[x]' in line:
                    id_list.append(line.split('---')[-1].strip())
    if i:
        subprocess.run(['rm',p])

# INTERACTIVE UPDATE
if not len(id_list):
    print('No modifications!')
else:
    print('Confirming modifications...')
for i in id_list:
    if i:
        # a = subprocess.run(f'beet ls -a id:{i}', shell=True, capture_output=True).stdout.decode('ascii')
        # decision = input(f'Have you listened to {a}?\n[Y]/N?\n')
        subprocess.run(f'beet modify -a id:{i} status=1', shell=True)

# GENERATE CSV
print('Generating CSV...')
subprocess.run(
    'beet bareasc -a -f "\$album @@@ \$albumartist @@@ \$genre @@@ \$mb_albumid @@@ \$original_year @@@ \$id" status:0 > ~/notes/data/music_library.csv',
    shell=True)


# READ FILE
print('Reading CSV...')
df = pd.read_csv('/home/matias/notes/data/music_library.csv',
                 delimiter='@@@',
                 engine='python',
                 names=['album','artist','genrelist','mbid','year','id'])
# SEPARATE GENRE AND CREATE LIST OF MENTIONNED GENRE
genre_lists = [[n.strip() for n in i.split(';')] for i in df['genrelist'].tolist()]
genre_mentions = [j for k in genre_lists for j in k]

# CREATE DICTIONNARY CONTAINING POPULARITY OF EACH GENRE
genre_dic = {k:0 for k in set(genre_mentions)}
for i in genre_mentions:
    genre_dic[i] += 1
dc = pd.DataFrame(pd.Series(genre_dic),columns=['count'])
dc.sort_values('count', ascending=False,inplace=True)
df['genre'] = [a if a else 'None' for a in [sorted(n, key=lambda x : dc.loc[x,'count'],
                                                   reverse=True)[0] for n in genre_lists]]
genre_dic['None'] = genre_dic['']

# CREATE A DICTIONANRY FOR THE 10 GENRE WITH MOST ALBUMS AND ANOTHER FOR THE REST
print(f'Ranking genres, {GENRE_NB} most frequent selected!')
sorted_genres = sorted({k:v for k,v in genre_dic.items() if k in df['genre'].tolist()},
                    key=lambda x : genre_dic[x], reverse=True)
try:
    sorted_genres.remove('None')
except ValueError:
    pass
solo_notes = sorted_genres[:GENRE_NB]
grouped_note = [i for i in sorted_genres if i not in solo_notes]+['None']

# GENERATE LINES FOR EACH GENRE MD_NOTE
df.sort_values(['artist','album'], inplace=True)
df.reset_index(drop=True,inplace=True)
genre_note_dic = {k: df[df['genre']==k].index.to_list() for k in solo_notes}
notes_content = {
    k : [f"- [ ] {df.loc[i,'artist']} --- {df.loc[i,'album']} --- {df.loc[i, 'id']}\n"
         for i in v] for k,v in genre_note_dic.items()}

# GENERATE LINES FOR THE GROUPED MD_NOTE
group_note_dic = {k: df[df['genre']==k].index.to_list() for k in grouped_note}
group_note_content_dic = {
    k : [f"- [ ] {df.loc[i,'artist']} --- {df.loc[i,'album']} --- {df.loc[i, 'id']}\n" for i in v]
    for k,v in group_note_dic.items()}
group_note_content = []
for k,v in group_note_content_dic.items():
    group_note_content += [f"# {k}\n"]
    group_note_content += v+['\n']

# GROUP FILE CONTENTS
all_notes_dic = notes_content.copy()
all_notes_dic['other'] = group_note_content

# WRITE FILES
print('Generating notes...')
rm_dic = {k:0 for k in all_notes_dic.keys()}
rm_dic['other'] = 1

index_file_links = {}
for k in all_notes_dic.keys():
    path = f"albums_to_listen_{k.replace(' ','_')}.md"
    index_file_links[k] = (path,
                           len(all_notes_dic[k])-1-len(group_note_dic.keys())*2*rm_dic[k])
    with open(PATH+path, 'w') as f:
        f.writelines(all_notes_dic[k])

index_lines = [f'# [{k} ({n})]({v})\n' for k,(v,n) in index_file_links.items()]
with open(PATH+'albums_to_listen_INDEX.md', 'w') as f:
    f.writelines(index_lines)

# PROGRESS
all_nb = len(subprocess.run('beet bareasc -a',shell=True, capture_output=True).stdout.decode('ascii').split('\n')[:-1])
lis_nb = len(subprocess.run('beet bareasc -a status:1',shell=True, capture_output=True).stdout.decode('ascii').split('\n')[:-1])
print(f'You have listened to {lis_nb}/{all_nb} albums ({round(100*lis_nb/all_nb,1)} %)')
