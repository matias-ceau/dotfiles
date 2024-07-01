#! /usr/bin/env xonsh

#DOC#=2024-06=$deprecated$ "Scripts that find the information of other scripts / better C version"

import pandas as pd
import argparse

LANGS = {'python':'py', 'xonsh':'xsh', 'bash':'sh', '/sh':'sh'}
SCRIPT_FOLDER = $HOME+"/.scripts/"

# Function to extract information from the third line
def extract_info(path):
    info = {
        "FILE" : path.split('/')[-1],                     #p file path
        "EXT" : path.split('.')[-1],       #p file extension
        "SCRIPT": False,                   #  shebang
        "LANG": "",                        #  inside shebang 
        "DOC" : False,                     #D documented
        "DESCR": "",                       #D rofi/dmenu descr
        "TYPE": "",                        #D type of script
        "STATUS": "active",                #D archived, active?
        "HOST": True,                      #D executable here?
        "DATE": "",                        #D old, new
        "TAGS": "",                        #D theme
        "OK": True,                        #  error detected
        "MSG" : ""                         #  info on error
    }
    line1 = $(sed -n '1p' @(path))
    if line1.startswith('#!'):
        info["SCRIPT"] = True
        LANG = [i for i in LANGS.keys() if i in line1] 
        if len(LANG):
            info["LANG"] = LANG[0]
        else:
            info['LANG'] = ''
        if (not info['LANG']) or (info['EXT'] != LANGS[info["LANG"]]):
            info['OK'] = False
            info['MSG'] = 'Problem with file extension.\n'

        line3 = $(sed -n '3p' @(path))
        if line3.startswith("#DOC#"):
            info["DOC"] = True
            try:
                info['DESCR'] = ' '.join(line3.split(' ')[1:]).strip()[1:-1]
                line3 = line3.split(' ')[0] 
                if '@' in line3:
                    info['TYPE'] = line3.split('@')[1]
                if '$' in line3:
                    info['STATUS'] = line3.split('$')[1]
                if '~' in line3:
                    HOST = line3.split('~')[1]
                    if HOST != $HOSTNAME:
                        info['HOST'] = False
                if '=' in line3:
                    info['DATE'] = line3.split('=')[1]
                if '+' in line3:
                    info['TAGS'] = line3.split('+')[1]
            except Exception as e:
                info['OK'] = False
                info['MSG'] += f'No description! -- {e}\n'
        else:
            info['OK'] = False
            info['MSG'] += 'Shebang but no documentation!\n'
    return info

def create_df():
    paths = $(find @(SCRIPT_FOLDER) -type f).splitlines()
    list_of_dicts = [extract_info(p) for p in paths]
    cols_dtypes = {'FILE':str, 'EXT':str, 'SCRIPT':bool, 'LANG':str, 'DOC':bool, 'DESCR':str, 'TYPE':str, 'STATUS':str, 'HOST':bool, 'DATE':str, 'TAGS':str, 'OK':bool, 'MSG':str}
    dict = {k : pd.Series([i[k] for i in list_of_dicts]).astype(v) for k,v in cols_dtypes.items()}
    data = pd.DataFrame(dict)
    return data

df = create_df()

# Argument parsing
parser = argparse.ArgumentParser(description="Filter and format script file data.")
parser.add_argument('-c', '--columns', nargs='+', help='Filter columns in the format "COLUMN=VALUE"')
parser.add_argument('-f', '--format', type=str, help='Format string for output')
parser.add_argument('-p', '--print', action='store_true', help='Show the DataFrame')
parser.add_argument('-s', '--sort', nargs='+', help='Sort by column values (you can add "_" to reverse the sorting order)')

args = parser.parse_args()

# Sort by columns
if args.sort:
    for c in args.sort:
        if c[0] == '_':
            asc = False
            c = c[1:]
        else:
            asc = True
        df.sort_values(by=c, ascending=asc, inplace=True, kind='mergesort')

# Apply column filters
if args.columns:
    for col_filter in args.columns:
        if '=' in col_filter:
            column, value = col_filter.split('=')
            df = df[df[column] == value]
        elif '~' in col_filter:
            column, value = col_filter.split('~')
            df = df[df[columns] != value]
        else:
            df = df[df[col_filter] == True]

# Print formatted output
if args.format:
    for index, row in df.iterrows():
        # .format(**row) unpacks the Series row into keyword arguments for the format string
        print(args.format.format(**row))
elif args.print:
    from tabulate import tabulate
    print(tabulate(df, headers='keys', tablefmt='pretty'))
