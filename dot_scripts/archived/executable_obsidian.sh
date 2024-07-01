#!/bin/bash

#DOC#@RUN@$deprecated$ "Open any obsidian vault (replaced with xonsh script, kept for interoperability)"

# Vault names
vaults=("notes" "work" "psyris")  # Replace with your actual vault names

# Use dmenu to get the selected vault name
selected_vault=$(printf '%s\n' "${vaults[@]}" | dmenu -i -l 20 -p 'Select a vault:')

if [ -n "$selected_vault" ]; then
    obsidian "obsidian://open?vault=$selected_vault" &  # Open vault in background
else
    echo "No vault selected."
fi
