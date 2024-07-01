#!/usr/bin/python3

#DOC#@CLI@$in_progress$ "Show useful help for tmux"

import argparse
import configparser
import os
import re
import sys
import subprocess
import time
from fuzzywuzzy import process

# Paths
DATA_DIR = os.path.expanduser('~.scripts/config/tmux-help/data')
full_manpage_path = os.path.join(DATA_DIR, '_full-manpage.txt')
sections_path = os.path.join(DATA_DIR, '_sections.txt')
log_path = os.path.join(DATA_DIR, 'tmux-help.log')
last_checked_path = os.path.join(DATA_DIR, 'last_checked.log')

# Ensure necessary directories and files exist
def ensure_paths():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(full_manpage_path):
        open(full_manpage_path, 'w').close()
        print(f"Created {full_manpage_path}. Please populate it with the full tmux manpage content.")
    if not os.path.exists(sections_path):
        open(sections_path, 'w').close()
        print(f"Created {sections_path}. Please populate it with the sections of the tmux manpage.")
    if not os.path.exists(log_path):
        open(log_path, 'w').close()
    if not os.path.exists(last_checked_path):
        with open(last_checked_path, 'w') as f:
            f.write("0")
        print(f"Created {last_checked_path} to track the last time the manpage was checked.")



# Helper functions
def load_tmux_commands():
    if not os.path.exists(full_manpage_path) or not os.path.exists(sections_path):
        log_error("Manpage or sections file not found. Ensure the files exist and contain the tmux commands.")
        sys.exit(1)
    
    with open(full_manpage_path, 'r') as f:
        full_manpage = f.readlines()
    
    with open(sections_path, 'r') as f:
        sections = f.readlines()

def log_error(message):
    with open(log_path, 'a') as log_file:
        log_file.write(f"ERROR: {time.ctime()}: {message}\n")
    print(f"ERROR: {message}")

def log_info(message):
    with open(log_path, 'a') as log_file:
        log_file.write(f"INFO: {time.ctime()}: {message}\n")

def highlight_binding(command):
    match = re.search(r'^(C-b\s+)(.+)$', command)
    if match:
        return f"{match.group(1)}\033[1m{match.group(2)}\033[0m"
    return command

def list_commands(commands, original_order=False):
    if original_order:
        for command in commands:
            print(highlight_binding(command))
    else:
        themes = {
            "Navigation": [],
            "Editing": [],
            "File Management": [],
            "System Control": [],
            "Application Launching": [],
            "Custom Shortcuts": []
        }

        for command in commands:
            if 'move' in command or 'scroll' in command or 'switch' in command:
                themes["Navigation"].append(command)
            elif 'copy' in command or 'cut' in command or 'paste' in command or 'undo' in command or 'redo' in command or 'delete' in command:
                themes["Editing"].append(command)
            elif 'open' in command or 'save' in command or 'close' in command:
                themes["File Management"].append(command)
            elif 'volume' in command or 'brightness' in command or 'lock' in command:
                themes["System Control"].append(command)
            elif 'launch' in command:
                themes["Application Launching"].append(command)
            else:
                themes["Custom Shortcuts"].append(command)
        
        for theme, cmds in themes.items():
            if cmds:
                print(f"\n{theme}\n" + "-" * len(theme))
                for command in cmds:
                    print(highlight_binding(command))

def fuzzy_search(commands, keyword):
    results = process.extract(keyword, commands, limit=3)
    for command, _ in results:
        print(highlight_binding(command))

def exact_search(commands, keyword):
    results = [command for command in commands if keyword.lower() in command.lower()]
    for command in results:
        print(highlight_binding(command))

def search_key(commands, key):
    results = [command for command in commands if key.lower() in command.split()[1].lower()]
    if results:
        for command in results:
            print(highlight_binding(command))
    else:
        print(f"No command found for key: {key}")

def extract_keybindings(sections):
    keybindings = []
    # 
    #        if line.startswith('             '):
    #            keybindings.append(line.strip())
    return keybindings

def update_manpage():
    try:
        subprocess.run(["man", "-P", "cat", "tmux"], stdout=open(full_manpage_path, "w"), check=True)                                                                                                                      
        subprocess.run(["sh", "-c", "man tmux | grep -E '^[A-Z ]+$' | awk '{$1=$1};1'"], stdout=open(sections_path, "w"), check=True)                                                                                      
        subprocess.run(["date", "+%s"], stdout=open(last_checked_path, "w"), check=True)

        with open(full_manpage_path, 'r') as f:
            manpage = f.readlines()    
        with open(sections_path, 'r') as f:
            section_titles = [i.strip() for i in f.readlines()]
            
        indices = [n for n,p in enumerate(manpage) if p.strip() in section_titles] + [len(manpage)]
        indices = [(indices[i],indices[i+1]) for i in range(len(indices)-1)]
        
        for n,(s,(i,j)) in enumerate(zip(section_titles,indices)):
            with open(os.path.join(DATA_DIR, f"{n}-{s}.txt"), 'w') as f:
                f.writelines(manpage[i:j])
        log_info("Manpage and sections updated successfully.")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to update manpage or sections: {str(e)}")

def needs_update():
    with open(last_checked_path, 'r') as f:
        last_checked = int(f.read().strip())
    return (time.time() - last_checked) > 604800  # 604800 seconds = 1 week

def get_sections():
    sections = [f for f in os.listdir(DATA_DIR) if f.endswith('.txt') and re.match(r'\d+-', f)]
    sections = sorted(sections, key=lambda x : int(x.split('-')[0]))
    S_nb, S_na = {}, {}
    for section in sections:
        section_name = section.replace('.txt', '').split('-')[1]
        section_number = section.split('-')[0]
        S_nb[section_number] = section_name
        S_na[section_name] = section_number
    print(sections)
    return S_nb, S_na

def list_sections():
    S_nb, S_na = get_sections()
    for k,v in S_nb.items():
        print(f"{k:3} -  {v}")

def display_section(section):
    S_nb, S_na = get_sections()
    if section.isnumeric():
        try:
            section_number = section
            section = S_nb[section]
        except KeyError:
            print('Not in list of sections')
    else:
        try:
            section = section.upper()
            section_nb = S_na[section]
        except KeyError:
            print('Not a valid section name')
    section_file = os.path.join(DATA_DIR, f"{section_number}-{section}.txt")
    if os.path.exists(section_file):
        with open(section_file, 'r') as f:
            content = f.read()
        print(content)
    else:
        print(f"Section {section} not found.")


def main():
    ensure_paths()
    
    # Command-line interface
    parser = argparse.ArgumentParser(description='tmux-help: A script to assist with tmux commands')
    parser.add_argument('-L', '--list-tmux', action='store_true', help='List tmux commands in the original order')
    parser.add_argument('-f', '--find', metavar='ARG', type=str, help='Fuzzy search the keyword descriptions')
    parser.add_argument('-F', '--find-exact', metavar='ARG', type=str, help='Search for exact match (case insensitive)')
    parser.add_argument('-s', '--search', metavar='KEY', type=str, help='Search for the key and return the result')
    parser.add_argument('-u', '--update', action='store_true', help='Update tmux manpage and sections')
    parser.add_argument('-S', '--section', nargs='?', const=True, help='List all sections or display a specific section by number or name')
    
    args = parser.parse_args()
    
    # Main logic
    if args.update or needs_update():
        update_manpage()
        return
    try:
        commands = load_tmux_commands()
    except Exception as e:
        log_error(f"Failed to load tmux commands: {str(e)}")
        sys.exit(1)

    if args.list_tmux:
        list_commands(commands, original_order=True)
    elif args.find:
        fuzzy_search(commands, args.find)
    elif args.find_exact:
        exact_search(commands, args.find_exact)
    elif args.search:
        search_key(commands, args.search)
    elif args.section is not None:
        if args.section is True:
            list_sections()
        else:
            display_section(args.section)
    else:
        list_commands(commands)
        
if __name__ == "__main__":
    main()

