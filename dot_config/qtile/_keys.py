from _custom import NOTEBOOKS, scripts, show_power_menu
from libqtile import extension
from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.lazy import lazy as L

M = ["mod4"]
A = ["mod1"]
S = ["shift"]
C = ["control"]
brightnessdown, brightnessup = "XF86MonBrightnessDown", "XF86MonBrightnessUp"
volumedown, volumeup, mute = (
    "XF86AudioLowerVolume",
    "XF86AudioRaiseVolume",
    "XF86AudioMute",
)

keys = [
    ## Windows
    ### Navigation
    Key(M + A, "Home", L.next_screen(), desc="Go to next screen"),
    Key(M, "h", L.layout.left(), desc="Move focus to left"),
    Key(M, "l", L.layout.right(), desc="Move focus to right"),
    Key(M, "j", L.layout.down(), desc="Move focus down"),
    Key(M, "k", L.layout.up(), desc="Move focus up"),
    Key(M, "Tab", L.layout.next(), desc="Move window focus to other panes"),
    Key(
        M + A,
        "j",
        L.group.next_window(),
        desc="Move window focus to next window in group",
    ),
    Key(
        M + A,
        "k",
        L.group.prev_window(),
        desc="Move window focus to prev window in group",
    ),
    Key(
        M + S,
        "bracketright",
        L.spawn("qtile_window_to_group_and_switch.py -n"),
        desc="Send to next group and switch",
    ),
    Key(
        M + S,
        "bracketleft",
        L.spawn("qtile_window_to_group_and_switch.py -p"),
        desc="Send to previous group and switch",
    ),
    Key(M, "Right", L.screen.next_group(), desc="Cycle groups"),
    Key(M, "bracketright", L.screen.next_group(), desc="Cycle groups"),
    Key(M, "Left", L.screen.prev_group(), desc="Cycle groups"),
    Key(M, "bracketleft", L.screen.prev_group(), desc="Cycle groups"),
    Key(M, "grave", L.next_layout(), desc="Toggle between layouts"),
    Key(M + S, "grave", L.prev_layout(), desc="Toggle between layouts"),
    Key(M, "q", L.window.kill(), desc="Kill focused window"),
    Key(M + C, "r", L.reload_config(), desc="Reload the config"),
    Key(M + A, "r", L.restart(), desc="Restart qtile"),
    Key(M + A, "q", L.shutown(), desc="Shutdown qtile"),
    Key(
        M + C,
        "q",
        L.function(show_power_menu),
        desc="Qtile-extras pop up menu",  # TODO: modify the popup menu
    ),
    Key(
        M,
        "w",
        L.run_extension(extension.WindowList()),
        desc="List all windows",  # TODO: modify to use fzf
    ),
    ### Move
    Key(
        M + S,
        "h",
        L.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        M + S,
        "l",
        L.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(M + S, "j", L.layout.shuffle_down(), desc="Move window down"),
    Key(M + S, "k", L.layout.shuffle_up(), desc="Move window up"),
    Key(
        M + C,
        "h",
        L.layout.grow_left(),
        desc="Grow window to the left",
    ),
    ### Resize
    Key(
        M + C,
        "l",
        L.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key(M + C, "j", L.layout.grow_down(), desc="Grow window down"),
    Key(M + C, "k", L.layout.grow_up(), desc="Grow window up"),
    Key(
        M + C,
        "equal",
        L.layout.normalize(),
        desc="Reset all window sizes",
    ),
    # FLOATING WINDOWS
    Key(
        M,
        "minus",
        L.window.resize_floating(-60, -40).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Shrink and center floating",
    ),
    Key(
        M + S,
        "minus",
        L.window.resize_floating(-15, -10).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Shrink and center floating (small inc)",
    ),
    Key(
        M,
        "equal",
        L.window.resize_floating(60, 40).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Grow and center floating",
    ),
    Key(
        M + S,
        "equal",
        L.window.resize_floating(15, 10).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Grow and center floating (small increment)",
    ),
    # Toggle between split and unsplit sides of stack.
    Key(
        M,
        "Prior",
        L.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        M,
        "f",
        L.window.toggle_floating(),
        desc="Toggle floating",
    ),
    Key(
        M,
        "m",
        L.window.toggle_fullscreen(),
        desc="Toggle fullscreen",
    ),
    Key(
        M,
        "Down",
        L.spawn("qtile_dice_group.py"),
        desc=f"Switch to complimentary group (eg: c+n=7)",
    ),
    Key(
        M,
        "Up",
        L.screen.toggle_group(),
        desc=f"Switch to last group",
    ),
    ## Media keys / function keys (other than scratchpads)
    Key([], brightnessup, L.spawn("light -a 10"), desc="increase brightness"),
    Key(
        [],
        brightnessdown,
        L.spawn("light -U 10"),
        desc="Decrease brightness",
    ),
    Key(
        [],
        mute,
        L.spawn("amixer -q set Master toggle"),
        desc="Toggle mute with amixer",
    ),
    Key(
        [],
        volumedown,
        L.widget["volume"].decrease_vol(),
        desc="Lower volume",
    ),
    Key(
        [],
        volumeup,
        L.widget["volume"].increase_vol(),
        desc="Raise volume",
    ),
    Key(
        M,
        volumedown,
        L.spawn("xdotool mousemove_relative -- -50 0"),
        desc="Mouse left",
    ),
    Key(
        M,
        volumeup,
        L.spawn("xdotool mousemove_relative 50 0"),
        desc="Mouse right",
    ),
    Key(
        M + S,
        volumedown,
        L.spawn("xdotool mousemove_relative -- 0 -50"),
        desc="Mouse down",
    ),
    Key( M + S, volumeup, L.spawn("xdotool mousemove_relative 0 50"), desc="Mouse up",),
    Key( A, volumeup, L.spawn("xdotool click 5"), desc="Mouse down",),
    Key( A, volumedown, L.spawn("xdotool click 4"), desc="Mouse up",),
    Key( M, mute, L.spawn("xdotool click 1"), desc="Left click",),
    Key( M + S, mute, L.spawn("xdotool click 3"), desc="Right click",),
    # Key( M, "a", L.spawn("jgmenu_run"), desc="Jgmenu app list",),
    Key(M, "F2", L.spawn("wallpaper.sh --random"), desc="Wallpaper random"),
    Key(
        M + S,
        "F2",
        L.spawn("wallpaper.sh --previous"),
        desc="Wallpaper previous",
    ),
    Key(
        M + C,
        "F2",
        L.spawn("wallpaper.sh --gui"),
        desc="Wallpaper select with GUI (WIP)",
    ),
    Key(
        M + A,
        "F2",
        L.spawn("wallpaper.sh --select"),
        desc="Wallpaper select with fzf",
    ),
    ## Commands
    ### General
    Key(M + S, "d", L.spawn("dmenu_run -l 30"), desc="Run app with dmenu"),
    Key(
        M,
        "space",
        L.spawn("fzfmenu_run.sh"),
        desc="Basic app launcher (using fzfmenu)",
    ),
    Key(
        M + S,
        "space",
        L.spawn("rofi -show drun"),
        desc="Run app with rofi (desktop apps)",
        # TODO: change to something else (fzf)
    ),
    Key(
        M,
        "b",
        L.spawn('notify-send "Hello" "hihi"'),
        desc="Bookmarks menu (WIP)",
    ),  # TODO: (also add, auto format, copy/paste)
    # scripts
    Key(
        M,
        "semicolon",
        L.spawn("script_launcher.sh"),
        desc="Launch and edit user scripts",
    ),
    Key(M, "Return", L.spawn(["kitty", "-1"]), desc="Launch terminal"),
    Key(
        M + S,
        "t",
        L.spawn(["alacritty", "-T", "dis_term"]),
        desc="Launch secondary terminal",
    ),
    Key(
        M,
        "t",
        L.spawn(["alacritty", "-T", "floating"]),
        desc="Launch floating terminal",
    ),
    Key(
        M,
        "o",
        L.spawn("obsidian-vault-selector.sh"),
        desc="Open obsidian vault",
    ),
    Key(
        M,
        "Print",
        L.spawn("flameshot full"),
        desc="Take screenshot of the full screen",
    ),
    Key(
        M + C,
        "Print",
        L.spawn("flameshot gui"),
        desc="Take screenshot of selected area",
    ),
    # quicklaunch
    KeyChord(
        M,
        "x",
        [
            Key(
                [],
                "h",
                L.spawn(
                    "notify-send 'HELP' 'This will be a help menu\nExit with <q> or <C-c>'"
                ),
            ),
            Key(
                [],
                "n",
                L.run_extension(
                    extension.CommandSet(commands=NOTEBOOKS, dmenu_lines=30)
                ),
            ),  # TODO: change notebook to custom script
            Key(
                S,
                "n",
                L.spawn("jupyter_new_notebook.xsh"),
                desc="Launch new notebook",
            ),
            Key(
                C,
                "c",
                L.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                [],
                "q",
                L.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                M,
                "less",
                L.ungrab_all_chords(),
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
        M,
        "s",
        [
            Key(
                [],
                "h",
                L.spawn(
                    "notify-send 'HELP' 'This will be a help menu\nExit with <q> or <C-c>'"
                ),
            ),
            Key(
                [],
                "c",
                L.spawn("urxvt -T floating -e tmux attach -t MUSIC:cmus"),
                desc="attach tmux",
            ),
            Key([], "Right", L.spawn("cmus-remote -n"), desc="next song"),
            Key(
                C,
                "Right",
                L.spawn(f"{scripts}/next_album.xsh"),
                desc="Next album",
            ),
            Key([], "Left", L.spawn("cmus-remote -r"), desc="previous song"),
            Key([], "space", L.spawn("cmus-remote -u"), desc="play/pause"),
            Key(
                [],
                "s",
                L.spawn(
                    ["xterm", "-T", "floating", "-e", f"{scripts}/fzf_songlauncher.sh"]
                ),
                desc="select song",
            ),
            Key(
                [],
                "a",
                L.spawn(f"xterm -T floating -e {scripts}/fzf_albumlauncher.xsh"),
                desc="select song",
            ),
            Key(
                [],
                "r",
                L.spawn(f"{scripts}/random_album.xsh"),
                desc="select random album",
            ),
            Key(
                [],
                "p",
                L.spawn(f"{scripts}/playlist_player.xsh"),
                desc="play playlist",
            ),
            Key(
                A,
                "p",
                L.spawn(f"{scripts}/playlist_randomizer.xsh"),
                desc="play playlist in random order",
            ),
            Key(
                [],
                "q",
                L.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                C,
                "c",
                L.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                M,
                "s",
                L.ungrab_all_chords(),
                desc="Exit",
            ),
        ],
        name="cmus",
        mode=True,
        desc="Sound menu (music players)",
    ),
    KeyChord(
        M,
        "F1",
        [
            Key(
                [],
                "h",
                L.spawn(
                    "notify-send 'HELP' 'This will be a help menu\nExit with <q> or <C-c>'"
                ),
            ),
            Key(
                [],
                "k",
                L.spawn(f"{scripts}/keyboard-help.sh"),
                desc="show keymap",
            ),
            Key(
                [],
                "q",
                L.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                C,
                "c",
                L.ungrab_all_chords(),
                desc="Exit",
            ),
            Key(
                M,
                "F1",
                L.ungrab_all_chords(),
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
        L.group["dock"].dropdown_toggle("terminal"),
        desc="Toggle dropdown terminal",
    ),
    # TODO make smth + F12 just do F12
    Key(
        M,
        "F11",
        L.group["dock"].dropdown_toggle("vimwiki"),
        desc="Toggle vimwiki",
    ),
    Key(
        M,
        "F10",
        L.group["dock"].dropdown_toggle("ranger"),
        desc="Toggle ranger",
    ),
    Key(
        M,
        "F9",
        L.group["dock"].dropdown_toggle("sysmon"),
        desc="Toggle sysmon",
    ),
    Key(
        M,
        "c",
        L.group["scratch"].dropdown_toggle("chatbot"),
        desc="Toggle llm chatbot",
    ),
    Key(M, "n", L.group["scratch"].dropdown_toggle("note"), desc="Toggle note"),
    Key(
        M,
        "p",
        L.group["scratch"].dropdown_toggle("keepassxc"),
        desc="Toggle keepassxc",
    ),
    # TODO: add a keybinding to cycle through scratch windows
]
### Mouse

# Drag floating layouts.
mouse = [
    Drag(
        M,
        "Button1",
        L.window.set_position_floating(),
        start=L.window.get_position(),
    ),
    Drag(
        M,
        "Button3",
        L.window.set_size_floating(),
        start=L.window.get_size(),
    ),
    Click(M, "Button2", L.window.bring_to_front()),
]

## Groups

for g in "123456":
    keys.extend(
        [
            Key(
                M,
                g,
                L.group[g].toscreen(toggle=True),
                desc=f"Switch to group {g}",
            ),
            Key(
                M + S, g, L.window.togroup(g), desc=f"Move focused window to group {g}"
            ),
        ]
    )
