# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Table of Contents
- [Repository Overview](#repository-overview)
- [Chezmoi Application Inventory](#chezmoi-application-inventory)
- [Dotfiles Management with Chezmoi](#dotfiles-management-with-chezmoi)
- [Chezmoi Decision Tree](#chezmoi-decision-tree)
- [App-Specific Notes](#app-specific-notes)
- [Key Directories](#key-directories-gitsync)
- [Scripts Collection](#the-scripts-collection-scripts)

---

## Repository Overview

This directory (`~/.ai`) is the **dotfiles management basecamp** - a symlink aggregation hub pointing to various AI tool configurations and dotfiles. Dotfiles are managed with **chezmoi**. The scripts collection resides at `~/.scripts` (linked here as `.scripts`).

---

## Chezmoi Application Inventory

Quick reference for "is this managed by chezmoi?" decisions.

### Chezmoi-Managed Applications (~38 apps)
```
aichat      alacritty   bat         beets       btop        clipse
colortool   eww         fish        fontconfig  ghostty     git
gtk-2.0     gtk-3.0     hypr        kitty       lazygit     lsd
mako        mpd         mpv         ncmpcpp     neofetch    nvim
paru        picom       qpwgraph    qtile       qutebrowser ranger
rclone*     rofi        starship    swappy     tmux        waybar
wlogout     yazi
```
*\* indicates encrypted credentials*

### Standalone Configs (~55+ apps, NOT chezmoi-managed)
These live directly in `~/.config/` without chezmoi tracking:
- **Browsers**: chromium, brave, vivaldi, google-chrome
- **Audio/DAW**: ardour8, lmms, Tenacity, VCV Rack 2, carla, reaper
- **IDEs/Editors**: code-oss, cursor, windsurf, zed
- **Communication**: discord, Element, Signal, slack, telegram
- **Media**: obs-studio, spotify, vlc
- **System**: dconf, pulse, systemd, xsettingsd

### Quick Lookup Command
```bash
chezmoi managed | grep -i <appname>   # Check if managed
chezmoi unmanaged ~/.config           # List unmanaged config dirs
```

---

## Dotfiles Management with Chezmoi

Source state location: `~/.local/share/chezmoi`

### Key Commands
```bash
# Basic operations
chezmoi add <file>            # Add file to source state
chezmoi add --autotemplate    # Add with smart template detection
chezmoi add --recursive <dir> # Add entire directory
chezmoi add --exact <dir>     # Track directory exactly (delete extra files)
chezmoi add --encrypt <file>  # Add with GPG encryption (for secrets!)

# Editing
chezmoi edit <file>           # Edit managed file (auto-applies due to config)
chezmoi edit --watch <file>   # Edit with live apply on save

# Inspection
chezmoi diff                  # Preview pending changes
chezmoi status                # Show files that differ
chezmoi managed               # List all managed files
chezmoi unmanaged <path>      # List files NOT tracked

# Application
chezmoi apply -v              # Apply changes from source to target
chezmoi apply <file>          # Apply single file

# Management
chezmoi cd                    # Enter source directory
chezmoi forget <file>         # Stop managing file (keeps target)
chezmoi re-add <file>         # Update source from target
```

### Workflow for Claude Code (IMPORTANT)

**Editing dotfiles - safety-first approach:**
1. **Always edit the actual file first** (the symlink target, e.g., `~/.bashrc`)
   - This provides a safety net: `chezmoi apply` can revert bad changes
2. **Test the changes** - let user verify the modification works
3. **When satisfied**, persist to chezmoi source:
   ```bash
   chezmoi re-add ~/.bashrc
   # OR manually: cat ~/.bashrc > ~/.local/share/chezmoi/dot_bashrc
   ```
4. **Always commit and push** changes in chezmoi:
   ```bash
   chezmoi cd && git add -A && git commit -m "description" && git push
   ```

**Adding new files to chezmoi:**
```bash
chezmoi add ~/.newfile              # Add regular file
chezmoi add --encrypt ~/.secrets    # Add with GPG encryption (for secrets!)
```

**Reverting a bad change:**
```bash
chezmoi apply ~/.bashrc    # Restores from chezmoi source state
```

### Configuration Notes
- **Encryption**: GPG enabled (recipient key configured)
- **Diff/Merge**: Uses `nvim -d`
- **Auto-apply**: `edit.apply = true` - changes apply when editor closes

---

## Chezmoi Decision Tree

```
Is this config file managed by chezmoi?
│
├─ CHECK: chezmoi managed | grep <filename>
│
├─► MANAGED → Is it encrypted?
│   │
│   ├─► ENCRYPTED (*.age) → Use: chezmoi edit <file>
│   │                       (Edits decrypt, then re-encrypt on save)
│   │
│   └─► NOT ENCRYPTED → Safety-first workflow:
│                       1. Edit actual file directly
│                       2. Test changes
│                       3. chezmoi re-add <file>
│                       4. Commit in chezmoi repo
│
└─► NOT MANAGED → Want to add it?
    │
    ├─► YES → chezmoi add <file>
    │         (Use --encrypt for secrets, --exact for directories)
    │
    └─► NO → Edit directly, no chezmoi involvement
```

---

## App-Specific Notes

### nvim (~78 files)
- Complex Lua configuration in `lua/` subdirectories
- Be careful with the module structure - many interdependencies
- Test changes with `nvim --clean` to isolate issues
- Key files: `init.lua`, `lua/plugins/`, `lua/config/`

### hypr (Hyprland WM)
- Active window manager - test changes carefully
- `hyprland.conf` is the main config
- Reload with `hyprctl reload` after changes
- Monitor configs may need hardware-specific adjustments

### fish
- Recursive management: functions/, completions/, conf.d/
- Test functions with `source <file>` before committing
- `config.fish` sources other files - mind load order

### qutebrowser
- Has encrypted session data (bookmarks, history may contain sensitive URLs)
- `config.py` is the main config
- Use `:config-write-py` to export changes made via commands

### rclone (ENCRYPTED)
- Contains cloud storage credentials
- **Always** use `chezmoi edit` for this file
- Never output raw contents to logs or terminals

### tmux
- Plugin manager (tpm) in `~/.tmux/plugins/`
- `prefix + I` to install plugins after config changes

---

## Key Directories (Git/Sync)

| Directory | Type | Purpose |
|-----------|------|---------|
| `~/.scripts` | Git repo | Personal scripts collection |
| `~/.localdata` | Git repo (private) | Private local data |
| `~/.synced-repos` | Syncthing folder | Local repos synced across devices |
| `~/.local/share/chezmoi` | Git repo | Chezmoi source state |

---

## The Scripts Collection (`~/.scripts`)

A comprehensive collection of utility scripts for an Arch Linux environment with Qtile window manager. Focuses on workflow automation, system management, media control, and knowledge management.

**Scripts workflow:**
- Scripts live in `~/.scripts/bin/`
- `utils_update_symlinks.sh` symlinks executables to `~/.local/bin` (adds to PATH)
- After adding/modifying scripts: run `~/.scripts/meta/utils_update_symlinks.sh`
- Commit and push changes to the scripts git repo

### Scripts Commands

**Dependency Installation:**
```bash
~/.scripts/bin/install_dependencies.sh  # Uses paru, Arch-specific
```

**Script Integration (symlink to ~/.local/bin):**
```bash
~/.scripts/meta/utils_update_symlinks.sh
```

**Documentation Generation:**
```bash
~/.scripts/meta/llm-script-describer.py  # Regenerate AI docs and README index
```

**Launching Scripts:**
```bash
script_launcher.sh      # Fuzzy-find and launch with previews
dmenu_run_scripts.py    # Rofi-based launcher
```

**Git Workflows:**
```bash
sync-repo.sh            # Robust repo synchronization
gsi.sh                  # Interactive git sync
generate_commit_message.py  # AI-powered commit messages
```

### Architecture

```
~/.scripts/
├── bin/           # Primary executable scripts (~120 scripts)
├── lib/           # Shared environment (env.sh with Flexoki colors, FZF config)
├── meta/          # Infrastructure (symlinks, doc generation, cron)
├── docs/scripts/  # AI-generated markdown docs per script
├── src/           # Source for compiled utilities
├── dev/           # Experimental/WIP scripts
└── archived/      # Deprecated scripts
```

---

## Development Conventions

### Script Metadata
Include `#INFO:#` tag for documentation generators and launchers to parse.

### Environment Loading
Shell scripts should source the modular environment:
```bash
source "$SCRIPTS/lib/env.sh"
load_env "colors,fzf,paths"  # Or: load_env_full
```

### Key Environment Variables
- `$SCRIPTS` - Path to scripts directory
- `$GIT_REPOS` - Git repositories root
- `$LOCALDATA` - Local data storage

### Interactive UI Patterns
- **Terminal selection**: Use `fzf` with `bat` previews
- **Window manager selection**: Use `rofi` or `dmenu`
- **Floating terminals**: `alacritty` for script output

### Languages
- **Bash** (`.sh`) - Simple shell automation
- **Python** (`.py`) - Complex logic, uses `uv run --script` for deps
- **Xonsh** (`.xsh`) - Mix of Python logic and shell execution

### Python Script Pattern
```python
#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["colorama", "openai"]
# ///
```

---

## Documentation

Every script in `bin/` should have a corresponding `.md` in `docs/scripts/`, generated via `meta/llm-script-describer.py`. The script tracks changes via `script_info.json` hash comparisons.

## Color Theming

Uses Flexoki palette defined in `lib/env.sh`. Load with `load_env "colors"` to get `$FLEXOKI_*` and semantic color variables (`$PRIMARY_COLOR`, `$ERROR_COLOR`, etc.).

---

## Suggestions & Notes

Claude Code may leave suggestions as text notes:
- **Dedicated folder**: `~/.ai/suggestions/` for general improvements
- **In-context**: `NOTES.md` or `TODO.md` inside relevant directories

These are non-blocking recommendations for workflow improvements.
