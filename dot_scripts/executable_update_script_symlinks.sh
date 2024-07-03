#!/bin/bash

# Directories
SOURCE_DIRS=("$HOME/.scripts" "$HOME/.scripts/bin" "$HOME/.scripts/ext")
TARGET_DIR="$HOME/.local/bin"
LOG_FILE="$HOME/.scripts/log/symlinking.log"
DATA_FILE="$HOME/.scripts/data/symlink_data.csv"

# Create necessary directories if they don't exist
mkdir -p "$(dirname "$LOG_FILE")"
mkdir -p "$(dirname "$DATA_FILE")"

# Initialize the CSV file
echo "Original Path,Symlink,Command Name" > "$DATA_FILE"

# Function to log errors with date
log_error() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Symlink function
create_symlinks() {
    for DIR in "${SOURCE_DIRS[@]}"; do
        for FILE in $(find "$DIR/" -type f -executable 2>/dev/null); do
            BASENAME=$(basename "$FILE")
            SYMLINK="$TARGET_DIR/$BASENAME"

            if [ -e "$SYMLINK" ]; then
                if [ "$(readlink "$SYMLINK")" != "$FILE" ]; then
                    log_error "Conflict: $SYMLINK already exists and links to a different file."
                fi
            elif [ -L "$SYMLINK" ]; then
                if [ "$(readlink "$SYMLINK")" != "$FILE" ]; then
                    log_error "Conflict: $SYMLINK is a different symlink."
                fi
            else
                ln -s "$FILE" "$SYMLINK" && echo "$FILE,$SYMLINK,$BASENAME" >> "$DATA_FILE"
            fi
        done
    done
}

# Remove broken symlinks and log
remove_broken_symlinks() {
    for SYMLINK in "$TARGET_DIR"/*; do
        if [ -L "$SYMLINK" ] && [ ! -e "$SYMLINK" ]; then
            log_error "Removed broken symlink: $SYMLINK"
            rm "$SYMLINK"
        fi
    done
}

# Run functions
create_symlinks
remove_broken_symlinks

echo "Symlinking completed."

