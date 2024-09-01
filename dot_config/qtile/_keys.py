from _custom import NOTEBOOKS, scripts, show_power_menu
from libqtile import extension
from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.lazy import lazy

keys = [
    ## Windows
    ### Navigation
    Key(["mod4", "control"], "Home", lazy.next_screen(), desc="Go to next screen"),
    Key(["mod4"], "h", lazy.layout.left(), desc="Move focus to left"),
    Key(["mod4"], "l", lazy.layout.right(), desc="Move focus to right"),
    Key(["mod4"], "j", lazy.layout.down(), desc="Move focus down"),
    Key(["mod4"], "k", lazy.layout.up(), desc="Move focus up"),
    Key(["mod4"], "Tab", lazy.layout.next(), desc="Move window focus to other panes"),
    Key(
        ["mod4", "mod1"],
        "j",
        lazy.group.next_window(),
        desc="Move window focus to next window in group",
    ),
    Key(
        ["mod4", "mod1"],
        "k",
        lazy.group.prev_window(),
        desc="Move window focus to prev window in group",
    ),
    Key(["mod4"], "Right", lazy.screen.next_group(), desc="Cycle groups"),
    Key(["mod4"], "Left", lazy.screen.prev_group(), desc="Cycle groups"),
    Key(["mod4"], "grave", lazy.next_layout(), desc="Toggle between layouts"),
    Key(["mod4", "shift"], "grave", lazy.prev_layout(), desc="Toggle between layouts"),
    Key(["mod4"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(["mod4", "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key(
        ["mod4", "control"],
        "q",
        lazy.function(show_power_menu),
        desc="Qtile-extras pop up menu",  # TODO: modify the popup menu
    ),
    Key(
        ["mod4"],
        "w",
        lazy.run_extension(extension.WindowList()),
        desc="List all windows",  # TODO: modify to use fzf
    ),
    ### Move
    Key(
        ["mod4", "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        ["mod4", "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(["mod4", "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key(["mod4", "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        ["mod4", "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    ### Resize
    Key(
        ["mod4", "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key(["mod4", "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key(["mod4", "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key(
        ["mod4", "control"],
        "equal",
        lazy.layout.normalize(),
        desc="Reset all window sizes",
    ),
    # FLOATING WINDOWS
    Key(
        ["mod4"],
        "minus",
        lazy.window.resize_floating(-60, -40).when(when_floating=True),
        lazy.window.center().when(when_floating=True),
        desc="Shrink and center floating",
    ),
    Key(
        ["mod4", "shift"],
        "minus",
        lazy.window.resize_floating(-15, -10).when(when_floating=True),
        lazy.window.center().when(when_floating=True),
        desc="Shrink and center floating (small inc)",
    ),
    Key(
        ["mod4"],
        "equal",
        lazy.window.resize_floating(60, 40).when(when_floating=True),
        lazy.window.center().when(when_floating=True),
        desc="Grow and center floating",
    ),
    Key(
        ["mod4", "shift"],
        "equal",
        lazy.window.resize_floating(15, 10).when(when_floating=True),
        lazy.window.center().when(when_floating=True),
        desc="Grow and center floating (small increment)",
    ),
    # Toggle between split and unsplit sides of stack.
    Key(
        ["mod4"],
        "Prior",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        ["mod4"],
        "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating",
    ),
    Key(
        ["mod4"],
        "m",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen",
    ),
    Key(
        ["mod4"],
        "Down",
        lazy.spawn("qtile-dice-group.sh"),
        desc=f"Switch to complimentary group (eg: c+n=7)",
    ),
    Key(
        ["mod4"],
        "Up",
        lazy.screen.toggle_group(),
        desc=f"Switch to complimentary group (eg: c+n=7)",
    ),
    ## Media keys / function keys (other than scratchpads)
    Key(
        [], "XF86MonBrightnessUp", lazy.spawn("light -A 10"), desc="Increase brightness"
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("light -U 10"),
        desc="Decrease brightness",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer -q set Master toggle"),
        desc="Toggle mute with amixer",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 0 sset Master 1- unmute"),
        desc="Lower volume",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 0 sset Master 1+ unmute"),
        desc="Raise volume",
    ),
    Key(
        ["mod4"],
        "a",
        lazy.spawn("jgmenu_run"),
        desc="Jgmenu app list",
    ),
    Key(["mod4"], "F2", lazy.spawn("wallpaper.sh --random"), desc="Wallpaper random"),
    Key(
        ["mod4", "shift"],
        "F2",
        lazy.spawn("wallpaper.sh --previous"),
        desc="Wallpaper previous",
    ),
    Key(
        ["mod4", "control"],
        "F2",
        lazy.spawn("wallpaper.sh --gui"),
        desc="Wallpaper select with GUI (WIP)",
    ),
    Key(
        ["mod4", "mod1"],
        "F2",
        lazy.spawn("wallpaper.sh --select"),
        desc="Wallpaper select with fzf",
    ),
    ## Commands
    ### General
    Key(
        ["mod4", "shift"], "d", lazy.spawn("dmenu_run -l 30"), desc="Run app with dmenu"
    ),
    Key(
        ["mod4"],
        "space",
        lazy.spawn("fzfmenu_run.sh"),
        desc="Basic app launcher (using fzfmenu)",
    ),
    Key(
        ["mod4", "shift"],
        "space",
        lazy.spawn("rofi -show drun"),
        desc="Run app with rofi (desktop apps)",
        # TODO: change to something else (fzf)
    ),
    Key(
        ["mod4"],
        "b",
        lazy.spawn('notify-send "Hello" "hihi"'),
        desc="Bookmarks menu (WIP)",
    ),  # TODO: (also add, auto format, copy/paste)
    # scripts
    Key(
        ["mod4"],
        "x",
        lazy.spawn("script_launcher.sh"),
        desc="Launch and edit user scripts",
    ),
    Key(["mod4"], "Return", lazy.spawn(["kitty", "-1"]), desc="Launch terminal"),
    Key(
        ["mod4", "shift"],
        "t",
        lazy.spawn(["alacritty", "-T", "dis_term"]),
        desc="Launch secondary terminal",
    ),
    Key(
        ["mod4"],
        "t",
        lazy.spawn(["alacritty", "-T", "floating"]),
        desc="Launch floating terminal",
    ),
    Key(
        ["mod4"],
        "o",
        lazy.spawn("obsidian-vault-selector.sh"),
        desc="Open obsidian vault",
    ),
    Key(
        ["mod4"],
        "Print",
        lazy.spawn("flameshot full"),
        desc="Take screenshot of the full screen",
    ),
    Key(
        ["mod4", "control"],
        "Print",
        lazy.spawn("flameshot gui"),
        desc="Take screenshot of selected area",
    ),
    # quicklaunch
    KeyChord(
        ["mod4"],
        "less",
        [
            Key(
                [],
                "h",
                lazy.spawn(
                    "notify-send 'HELP' 'This will be a help menu\nExit with <q> or <C-c>'"
                ),
            ),
            Key(
                [],
                "n",
                lazy.run_extension(
                    extension.CommandSet(commands=NOTEBOOKS, dmenu_lines=30)
                ),
            ),  # TODO: change notebook to custom script
            Key(
                ["shift"],
                "n",
                lazy.spawn("jupyter_new_notebook.xsh"),
                desc="Launch new notebook",
            ),
            Key(
                ["control"],
                "c",
                lazy.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                [],
                "q",
                lazy.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                ["mod4"],
                "less",
                lazy.ungrab_all_chords(),
                desc="Exit",
            ),
        ],
        name="quicklaunch",
        mode=True,
        desc="Launch menu",
    ),
    # CMUS
    # TODO add seek etc
    ### Chords
    KeyChord(
        ["mod4"],
        "s",
        [
            Key(
                [],
                "h",
                lazy.spawn(
                    "notify-send 'HELP' 'This will be a help menu\nExit with <q> or <C-c>'"
                ),
            ),
            Key(
                [],
                "c",
                lazy.spawn("urxvt -T floating -e tmux attach -t MUSIC:cmus"),
                desc="attach tmux",
            ),
            Key([], "Right", lazy.spawn("cmus-remote -n"), desc="next song"),
            Key(
                ["control"],
                "Right",
                lazy.spawn(f"{scripts}/next_album.xsh"),
                desc="Next album",
            ),
            Key([], "Left", lazy.spawn("cmus-remote -r"), desc="previous song"),
            Key([], "space", lazy.spawn("cmus-remote -u"), desc="play/pause"),
            Key(
                [],
                "s",
                lazy.spawn(
                    ["xterm", "-T", "floating", "-e", f"{scripts}/fzf_songlauncher.sh"]
                ),
                desc="select song",
            ),
            Key(
                [],
                "a",
                lazy.spawn(f"xterm -T floating -e {scripts}/fzf_albumlauncher.xsh"),
                desc="select song",
            ),
            Key(
                [],
                "r",
                lazy.spawn(f"{scripts}/random_album.xsh"),
                desc="select random album",
            ),
            Key(
                [],
                "p",
                lazy.spawn(f"{scripts}/playlist_player.xsh"),
                desc="play playlist",
            ),
            Key(
                ["mod1"],
                "p",
                lazy.spawn(f"{scripts}/playlist_randomizer.xsh"),
                desc="play playlist in random order",
            ),
            Key(
                [],
                "q",
                lazy.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                ["control"],
                "c",
                lazy.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                ["mod4"],
                "s",
                lazy.ungrab_all_chords(),
                desc="Exit",
            ),
        ],
        name="cmus",
        mode=True,
        desc="Sound menu (music players)",
    ),
    KeyChord(
        ["mod4"],
        "F1",
        [
            Key(
                [],
                "h",
                lazy.spawn(
                    "notify-send 'HELP' 'This will be a help menu\nExit with <q> or <C-c>'"
                ),
            ),
            Key(
                [],
                "k",
                lazy.spawn(f"{scripts}/keyboard-help.sh"),
                desc="show keymap",
            ),
            Key(
                [],
                "q",
                lazy.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                ["control"],
                "c",
                lazy.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                ["mod4"],
                "F1",
                lazy.ungrab_all_chords(),
                desc="Exit",
            ),
        ],
        name="help",
        mode=True,
        desc="Help menu for this qtile config",
    ),
    ### Scratchpads
    Key(
        [],
        "F12",
        lazy.group["dock"].dropdown_toggle("terminal"),
        desc="Toggle dropdown terminal",
    ),
    # TODO make smth + F12 just do F12
    Key(
        ["mod4"],
        "F11",
        lazy.group["dock"].dropdown_toggle("vimwiki"),
        desc="Toggle vimwiki",
    ),
    Key(
        ["mod4"],
        "F10",
        lazy.group["dock"].dropdown_toggle("ranger"),
        desc="Toggle ranger",
    ),
    Key(
        ["mod4"],
        "F9",
        lazy.group["dock"].dropdown_toggle("sysmon"),
        desc="Toggle sysmon",
    ),
    Key(
        ["mod4"],
        "c",
        lazy.group["scratch"].dropdown_toggle("chatbot"),
        desc="Toggle llm chatbot",
    ),
    Key(
        ["mod4"], "n", lazy.group["scratch"].dropdown_toggle("note"), desc="Toggle note"
    ),
    Key(
        ["mod4"],
        "p",
        lazy.group["scratch"].dropdown_toggle("keepassxc"),
        desc="Toggle keepassxc",
    ),
    # TODO: add a keybinding to cycle through scratch windows
]
### Mouse

# Drag floating layouts.
mouse = [
    Drag(
        ["mod4"],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        ["mod4"],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click(["mod4"], "Button2", lazy.window.bring_to_front()),
]

## Groups

for g in "123456":
    keys.extend(
        [
            Key(
                ["mod4"],
                g,
                lazy.group[g].toscreen(toggle=True),
                desc=f"Switch to group {g}",
            ),
            Key(
                ["mod4", "shift"],
                g,
                lazy.window.togroup(g),
                desc=f"Move focused window to group {g}",
            ),
        ]
    )