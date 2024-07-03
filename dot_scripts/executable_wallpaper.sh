#! /usr/bin/bash

#DOC#@RUN@=2024-07= "Pick random wallpaper from wallpaper list"

# Default wallpaper
DEFAULT_WALLPAPER="$HOME/.wallpapers/_toitssuze.jpg"
CACHE="/home/matias/.cache/wallpapers.log"

# Function to set wallpaper
set_wallpaper() {
    feh --bg-scale "$1" && notify-send -t 3000 -r 1212 "Script" "Changed wallpaper!\n<b>$(basename "$1")</b>"
    echo "$1" >> "$CACHE"
}

# Parse arguments
case "$1" in
    --random)
        wallpaper=$(find ~/.wallpapers/ -type f | shuf -n 1)
        set_wallpaper "$wallpaper"
        ;;
    --select)
        wallpaper=$(find ~/.wallpapers/ -type f | fzfmenu.sh)
# -i -l 10)
        [ -n "$wallpaper" ] && set_wallpaper "$wallpaper"
        ;;
    --previous)
        n=${2:-1}
        n=$((n + 1))
        wallpaper=$(tail -n "$n" ~/.cache/wallpapers.log | head -n 1)
        sed -i "$(($(wc -l < $CACHE) - $n + 1)),\$d" "$CACHE"
        [ -n "$wallpaper" ] && set_wallpaper "$wallpaper"
        ;;
    --gui)
        wallpaper=$(find ~/.wallpapers/ -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.jpeg" \) -printf "%f\n%p\n" | \
            yad --list \
                --title="Select a wallpaper" \
                --width=400 --height=500 \
                --column="Filename" \
                --column="Path":HD \
                --hide-column=2 \
                --print-column=2 \
                --no-headers)
        if [ -n "$wallpaper" ]; then
            yad --image="$wallpaper" \
                --title="Preview" \
                --width=800 --height=600 \
                --button="Set as wallpaper:0" \
                --button="Cancel:1"
            if [ $? -eq 0 ]; then
                set_wallpaper "$wallpaper"
            fi
        fi
        ;;
   *)
       set_wallpaper "$DEFAULT_WALLPAPER"
       ;;
esac

# Remove successive duplicate entries
awk '!seen[$0]++' "$CACHE" > "$CACHE.tmp" && mv "$CACHE.tmp" "$CACHE"
