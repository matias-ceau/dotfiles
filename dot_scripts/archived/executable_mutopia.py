#! /usr/bin/python3

#DOC#@CLI@$deprecated$ "custom script to query mutopia"

import os
import pandas as pd
import sys


def query_mutopia(path='/home/matias/HDD2/DATA/MUSIC/mutopiaproject/'):
    dic = {a : c for a,b,c in os.walk(path) if c}
    files = [f"{k}/{i}" for k,v in dic.items() for i in v]
    cand_ext = [f.split('.')[-1] for f in files] \
        + [f.split('-')[-1] for f in files if '-' in f] \
        + ['-'.join(f.split('-')[-2:]) for f in files if len(f.replace('-','')) == (len(f) - 2)]
    s = pd.Series(cand_ext).value_counts()
    ext = s[s>30].index.tolist()
    extensions = [sorted([i for i in ext if a[-1*len(i):] == i],key=len) for a in files]
    short_ext = [a[0] for a in extensions]
    long_ext = [a[-1] if len(a)>1 else '' for a in extensions]
    composer = [a.replace(path,'').split('/')[0] for a in files]
    filename_x = [a.split('/')[-1].split('__')[-1] for a in files]
    filename = [a[:-1*(len(j)+1)] if j else a[:-1*(len(i)+1)] for a,i,j in zip(filename_x, short_ext, long_ext)]
    fold  = [i.replace(f"{path}{c}/",'').replace(f,'') for c,i,f in zip(composer,files,filename_x)]
    folder1 = [i.split('__')[0] if i else '' for i in fold]
    folders = ['__'.join(i.split('__')[1:]) if len(i.split('__'))>1 else '' for i in fold]
    ID = [f"{c}{'__' if f1 else ''}{f1}{'__' if f else ''}{f}__{n}" for c,f1,f,n in zip(composer, folder1, folders, filename)]
    size = [os.path.getsize(f) for f in files]
    df = pd.DataFrame(
        {'composer':composer,
         'ID': ID,
         'folder1' : folder1,
         'folders' : folders,
         'filename' : filename,
         'path':files,
         'short_ext' :short_ext,
         'long_ext':long_ext,
         'filesize': size
         })
    print(df)
    return df

if __name__ == '__main__':
    if len(sys.argv) > 1:
        query_mutopia(sys.argv[1])
    else:
        query_mutopia()
