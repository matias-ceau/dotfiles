#! /usr/bin/python3

#DOC#@RUN@~karjala~ "Custom script to copy music to Mechen"

import subprocess
from subprocess import PIPE
import os
import pandas as pd
import random
from getpass import getpass

#get pass
password = getpass('Password pliz: ')

# define mp3 player max space
MAX_SPACE = 50 * 1024**2
player_path = '/home/matias/MECHEN'

# get not listened to albums and their paths
album_query = subprocess.run('beet ls -ap status:0', shell=True, capture_output=True)
album_paths = album_query.stdout.decode('ascii').splitlines()
short_paths = [i.replace('/home/matias/music/','') for i in album_paths]
print(f"{len(album_paths)} not listened to")

# calculate sizes
sizes = [subprocess.run(['du','-sk',i],capture_output=True) for i in album_paths]
sizes = [int(i.stdout.decode('ascii').split('\t')[0]) for i in sizes]
print(f"Total size equal to {round(sum(sizes)/1024/1024,2)} GB")

# get artists
artist = [i.split('/')[4] for i in album_paths]

# create df
df = pd.DataFrame({'path' : album_paths,
                   'short_path' : short_paths,
                   'artist' : artist,
                   'size' : sizes})

# get albums already on device
artists_on_device = [i for i in os.listdir(player_path) if os.path.isdir(i)]
albums_on_device = [[f"{i}/{b}" for b in os.listdir(os.path.join(player_path,i))]
                    for i in artists_on_device]

albums_on_device = [i for j in albums_on_device for i in j]

# clean up dataframe
def drop_random_artist(df):
    to_drop = random.choice(list(set(df.artist)))
    print(to_drop)
    if to_drop in artists_on_device:
        return df
    else:
        return df[df['artist']!=to_drop]

def df_too_big(df):
    return df['size'].sum() > MAX_SPACE

while df_too_big(df):
    print(f'Too much data, removing:')
    df = drop_random_artist(df)


# remove unecessary albums
for i in albums_on_device:
    if i not in df['short_path'].to_list():
        proc = subprocess.Popen(['sudo','-S','rm','-rf',os.path.join(player_path,i)],
                                stdin=PIPE, stdout=PIPE, stderr=PIPE)
        proc.communicate(password.encode())

# remove empty folder
for i in os.listdir(player_path):
    p = os.path.join(player_path, i)
    if os.path.isdir(p):
        if not os.listdir(p):
            proc = subprocess.Popen(['sudo','-S','rm','-rf',p],
                                stdin=PIPE, stdout=PIPE, stderr=PIPE)
            proc.communicate(password.encode())

#generate artist and album folders
print('Creating folders...')
for i in df['short_path'].to_list():
    proc = subprocess.Popen(['sudo','-S','mkdir','-p',os.path.join(player_path,i)],
                                stdin=PIPE, stdout=PIPE, stderr=PIPE)
    proc.communicate(password.encode())

# rsync everything
nb_albums = len(df)
for n,i in enumerate(df['short_path'].to_list()):
    print(f"Rsyncing {i} ({n+1}/{nb_albums})")
    proc = subprocess.Popen(['sudo','-S','rsync','-rvu', '--delete',
                             os.path.join('/home/matias/music',i)+'/', #important for rsync to work properly
                             os.path.join(player_path,i)],
                                stdin=PIPE, stdout=PIPE, stderr=PIPE)
    proc.communicate(password.encode())
