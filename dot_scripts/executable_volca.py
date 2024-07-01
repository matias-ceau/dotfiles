#! /usr/bin/python3

#DOC#@RUN@ "Script to transfer samples to Korg volca sample 2" 

import os
import sys

folder = open('/home/matias/audio/SAMPLES/volca/log.txt','r').readlines()[-1][:-1]
path = f"/home/matias/audio/SAMPLES/volca/{folder}"
if 'output' not in os.listdir(path):
    os.system(f'mkdir {path}/output')
for n in range(len(os.listdir(path))):
    if '.wav' in os.listdir(path)[n]:
        nn = str(n)
        if len(nn) == 1: nn = '0'+nn
        cmd = f'''\
                sox "{path}/{os.listdir(path)[n]}" -r 33000 -c 1 -b 16 "{path}/output/{nn}_{os.listdir(path)[n]}"\
                '''
        os.system(cmd) 
