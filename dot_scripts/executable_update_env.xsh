#! /usr/bin/xonsh

#DOC#+api+=2024-06= "Update env file for storing api keys"

def update_env():
    apikeys_dict = {k:v for k,v in ${...}.items() if k[-7:]=='API_KEY'}
    apikeys_content = '\n'.join([f"{k}={v}" for k,v in apikeys_dict.items()])+'\n'
    with open($HOME+'/.env','w') as f:
        f.write(apikeys_content) 

update_env()
