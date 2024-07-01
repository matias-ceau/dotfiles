#/usr/bin/python

#DOC#@CLI@$deprecated$ "Custom help for ollama"

import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from colorama import init, Fore, Style
import textwrap
import argparse
import re
from datetime import timedelta
import warnings



# Suppress specific warnings                                                                                                                       
warnings.filterwarnings("ignore", category=UserWarning, module="pandas")                                                                           
warnings.filterwarnings("ignore", category=UserWarning, module="numpy")  

# Initialize colorama
init(autoreset=True)

# Define the URL
url = "https://ollama.com/library?sort=popular"

# Function to convert download numbers to float
def convert_downloads(download_str):
    download_str = download_str.split('\n')[0]
    if 'K' in download_str:
        return float(download_str.replace('K', '')) * 1_000, download_str
    elif 'M' in download_str:
        return float(download_str.replace('M', '')) * 1_000_000, download_str
    elif ',' in download_str:
        return float(download_str.replace(',', '')), download_str
    else:
        return float(download_str), download_str

# Function to convert time strings to number of days
def convert_last_updated(time_str):
    time_str = time_str.split('\n')[-1].strip()
    match = re.match(r"(\d+) (\w+)", time_str)
    if match:
        number, unit = match.groups()
        number = int(number)
        if ('month' in unit) or ('months' in unit):
            return number * 30, time_str
        elif ('week' in unit) or ('weeks' in unit):
            return number * 7, time_str
        elif ('day' in unit) or ('days' in unit):
            return number, time_str
    return 0, 'Unknown'

# Argument parser setup
parser = argparse.ArgumentParser(description='Scrape and display Ollama models.')
parser.add_argument('-p', '--popularity', action='store_true', help='Sort by popularity (number of downloads)')
parser.add_argument('-n', '--newest', action='store_true', help='Sort by most recently updated')
parser.add_argument('-a', '--all', action='store_true', help='Show all models')
parser.add_argument('-l', '--limit', type=int, default=10, help='Limit to N models (default: 5)')
parser.add_argument('-d', '--describe', type=str, help='Show full description of the specified model name')
args = parser.parse_args()

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all model containers
    model_containers = soup.select('li.flex')
    
    # Extract the model names, descriptions, downloads, and last updated info
    model_list = []
    for container in model_containers:
        model_name_element = container.select_one('a:nth-child(1) > h2:nth-child(1) > span:nth-child(1)')
        model_description_element = container.select_one('a:nth-child(1) > div:nth-child(2) > p:nth-child(1)')
        downloads_element = container.select_one('a:nth-child(1) > div:nth-child(2) > p:nth-child(3) > span:nth-child(1)')
        last_updated_element = container.select_one('a:nth-child(1) > div:nth-child(2) > p:nth-child(3) > span:nth-child(3)')
        
        if model_name_element and model_description_element and downloads_element and last_updated_element:
            model_name = model_name_element.text.strip()
            model_description = model_description_element.text.strip()
            downloads, formatted_downloads = convert_downloads(downloads_element.text.strip())
            last_updated, formatted_last_updated = convert_last_updated(last_updated_element.text.strip())
            wrapped_description = '\n'.join(textwrap.wrap(model_description, width=50))  # Adjust width as needed
            model_list.append({'Model Name': model_name, 
                               'Description': wrapped_description, 
                               'int_Downloads': downloads, 
                               'int_Last Updated': last_updated,
                               'Downloads' : formatted_downloads,
                               'Last Updated' : formatted_last_updated})
    
    # Convert the list to a DataFrame
    df = pd.DataFrame(model_list).astype({'Model Name': 'str', 
                                          'Description': 'str', 
                                          'int_Downloads': 'float', 
                                          'int_Last Updated': 'float',
                                          'Downloads' : 'str',
                                          'Last Updated' : 'str'})
    
    # Sort the DataFrame based on the arguments
    if args.popularity:
        df = df.sort_values(by='int_Downloads', ascending=False)
    if args.newest:
        df = df.sort_values(by='int_Last Updated')
    
    # Handle the describe argument
    if args.describe:
        described_model = df[df['Model Name'] == args.describe].drop(columns=['int_Downloads', 'int_Last Updated'])
        if not described_model.empty:
            table = tabulate(described_model, headers='keys', tablefmt='grid', showindex=False)
            print(Fore.CYAN + Style.BRIGHT + table)
        else:
            print(Fore.RED + f"Model {args.describe} not found.")
    else:
        # Handle the limit argument
        if not args.all:
            df = df.head(args.limit)
        
        # Remove the 'int_Downloads' and 'int_Last Updated' columns
        df = df.drop(columns=['int_Downloads', 'int_Last Updated'])
        
        # Print the DataFrame in a tabulated format with colors
        table = tabulate(df, headers='keys', tablefmt='grid', showindex=False)
        print(Fore.CYAN + Style.BRIGHT + table)
else:
    print(Fore.RED + f"Failed to retrieve the webpage. Status code: {response.status_code}")

