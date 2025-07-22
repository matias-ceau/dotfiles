from libqtile import extension

# Import standard Key and KeyChord, and modifier objects
from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.lazy import lazy as L

# Define standard modifier lists
M = ["mod4"]
A = ["mod1"]
S = ["shift"]
C = ["control"]

# Special keys (these names are already standard Xorg names)
brightnessdown, brightnessup = "XF86MonBrightnessDown", "XF86MonBrightnessUp"
volumedown, volumeup, mute = (
    "XF86AudioLowerVolume",
    "XF86AudioRaiseVolume",
    "XF86AudioMute",
)
forward, back = "XF86Forward", "XF86Back"  # Not used in keys, but kept

# Define the keys list using standard Key and KeyChord
keys = [
    # Navigation
    Key(M, "Home", L.next_screen(), desc="NextScr"),  # M-A-<Home> -> M+A, "Home"
    Key(M, "h", L.layout.left(), desc="Left"),  # M-h -> M, "h"
    Key(M, "l", L.layout.right(), desc="Right"),  # M-l -> M, "l"
    Key(M, "j", L.layout.down(), desc="Down"),  # M-j -> M, "j"
    Key(M, "k", L.layout.up(), desc="Up"),  # M-k -> M, "k"
    Key(M, "Tab", L.layout.next(), desc="NextPane"),  # M-<Tab> -> M, "Tab"
    Key(M + A, "j", L.group.next_window(), desc="NextWin"),  # M-A-j -> M+A, "j"
    Key(M + A, "k", L.group.prev_window(), desc="PrevWin"),  # M-A-k -> M+A, "k"
    Key(
        M + S,
        "bracketright",  # M-S-<bracketright> -> M+S, "bracketright"
        L.spawn("qtile_window_to_group_and_switch.py -n"),
        desc="NextGrp",
    ),
    Key(
        M + S,
        "bracketleft",  # M-S-<bracketleft> -> M+S, "bracketleft"
        L.spawn("qtile_window_to_group_and_switch.py -p"),
        desc="PrevGrp",
    ),
    # Fixed typo: M-<Righ>t -> M-<Right>
    Key(M, "Right", L.screen.next_group(), desc="NextGrp"),  # M-<Right> -> M, "Right"
    Key(
        M, "bracketright", L.screen.next_group(), desc="NextGrp"
    ),  # M-<bracketright> -> M, "bracketright"
    Key(M, "Left", L.screen.prev_group(), desc="PrevGrp"),  # M-<Left> -> M, "Left"
    Key(
        M, "bracketleft", L.screen.prev_group(), desc="PrevGrp"
    ),  # M-<bracketleft> -> M, "bracketleft"
    Key(
        M + C + A, "grave", L.next_layout(), desc="NextLay"
    ),  # M-C-A-<grave> -> M+C+A, "grave"
    Key(M + C + A, "1", L.to_layout_index(0), desc="Lay1"),  # M-C-A-1 -> M+C+A, "1"
    Key(M + C + A, "2", L.to_layout_index(1), desc="Lay2"),  # M-C-A-2 -> M+C+A, "2"
    Key(M + C + A, "3", L.to_layout_index(2), desc="Lay3"),  # M-C-A-3 -> M+C+A, "3"
    Key(M + C + A, "4", L.to_layout_index(3), desc="Lay4"),  # M-C-A-4 -> M+C+A, "4"
    Key(M + C + A, "5", L.to_layout_index(4), desc="Lay5"),  # M-C-A-5 -> M+C+A, "5"
    Key(M + C + A, "6", L.to_layout_index(5), desc="Lay6"),  # M-C-A-6 -> M+C+A, "6"
    Key(M, "q", L.window.kill(), desc="Kill"),  # M-q -> M, "q"
    Key(M + C, "r", L.reload_config(), desc="Reload"),  # M-C-r -> M+C, "r"
    Key(M + C + S, "r", L.restart(), desc="Restart"),  # M-C-S-r -> M+C+S, "r"
    Key(
        M + A, "q", L.shutdown(), desc="Shutdown"
    ),  # M-A-q -> M+A, "q" (Fixed L.shutown -> L.shutdown)
    # Key(M + C, "q", L.function(show_power_menu), desc="Power"), # M-C-q (Commented out as in original)
    # Key(M, "w", L.run_extension(extension.WindowList()), desc="WinList"), # M-w (Commented out as in original)
    # Move
    Key(M + S, "h", L.layout.shuffle_left(), desc="MvLeft"),  # M-S-h -> M+S, "h"
    Key(M + S, "l", L.layout.shuffle_right(), desc="MvRight"),  # M-S-l -> M+S, "l"
    Key(M + S, "j", L.layout.shuffle_down(), desc="MvDown"),  # M-S-j -> M+S, "j"
    Key(M + S, "k", L.layout.shuffle_up(), desc="MvUp"),  # M-S-k -> M+S, "k"
    # Resize
    Key(M + C, "h", L.layout.grow_left(), desc="GrLeft"),  # M-C-h -> M+C, "h"
    Key(M + C, "l", L.layout.grow_right(), desc="GrRight"),  # M-C-l -> M+C, "l"
    Key(M + C, "j", L.layout.grow_down(), desc="GrDown"),  # M-C-j -> M+C, "j"
    Key(M + C, "k", L.layout.grow_up(), desc="GrUp"),  # M-C-k -> M+C, "k"
    Key(
        M + C, "equal", L.layout.normalize(), desc="Norm"
    ),  # M-C-<equal> -> M+C, "equal"
    # Floating
    Key(
        M,
        "minus",  # M-<minus> -> M, "minus"
        L.window.resize_floating(-60, -40).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Float-",
    ),
    Key(
        M + S,
        "minus",  # M-S-<minus> -> M+S, "minus"
        L.window.resize_floating(-15, -10).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Float--",
    ),
    Key(
        M,
        "equal",  # M-<equal> -> M, "equal"
        L.window.resize_floating(60, 40).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Float+",
    ),
    Key(
        M + S,
        "equal",  # M-S-<equal> -> M+S, "equal"
        L.window.resize_floating(15, 10).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Float++",
    ),
    Key(M, "Prior", L.layout.toggle_split(), desc="Split"),
    Key(M, "f", L.window.toggle_floating(), desc="Float"),  # M-f -> M, "f"
    Key(M, "m", L.window.toggle_fullscreen(), desc="Full"),  # M-m -> M, "m"
    Key(M, "Up", L.screen.toggle_group(), desc="LastGrp"),  # M-<Up> -> M, "Up"
    Key(
        [], "XF86MonBrightnessUp", L.spawn("light -A 10"), desc="Bri+"
    ),  # <XF86MonBrightnessUp> -> [], "XF86MonBrightnessUp"
    Key([], "XF86MonBrightnessDown", L.spawn("light -U 10"), desc="Bri-"),
    Key([], "XF86AudioMute", L.spawn("amixer -q set Master toggle"), desc="Mute"),
    Key([], "XF86AudioLowerVolume", L.widget["volume"].decrease_vol(), desc="Vol-"),
    Key([], "XF86AudioRaiseVolume", L.widget["volume"].increase_vol(), desc="Vol+"),
    Key(M + S, "F2", L.spawn("wallpaper.sh --select"), desc="Wall"),
    # Commands
    Key(M + S, "d", L.spawn("dmenu_run -l 30"), desc="Dmenu"),  # M-S-d -> M+S, "d"
    Key(M, "space", L.spawn("fzfmenu_run.sh"), desc="Fzf"),  # M-<space> -> M, "space"
    Key(M + S, "space", L.spawn("fuzzel"), desc="Fuzzel"),
    Key(M, "semicolon", L.spawn("script_launcher.sh"), desc="Script"),
    Key(M, "Return", L.spawn(["kitty", "-1"]), desc="Term"),
    Key(
        M + S,
        "t",
        L.spawn(["footclient"]),
        desc="Term2",
    ),
    Key(
        M,
        "t",
        L.spawn("footclient --title=floating-TMUX"),
        desc="Tfloat",
    ),
    Key(M + S, "o", L.spawn("obsidian-vault-selector.sh"), desc="Obs"),
    Key(M, "o", L.spawn("qutebrowser"), desc="Qute"),
    Key(M, "b", L.spawn("opera"), desc="Opera"),
    Key([], "Print", L.spawn("screenshot.sh"), desc="Shot"),
    Key(S, "Print", L.spawn("screenshot.sh --select"), desc="Shot"),
    Key([], "F12", L.group["dock"].dropdown_toggle("terminal"), desc="STerm"),
    Key(M, "F11", L.group["dock"].dropdown_toggle("nvim"), desc="SNvim"),
    Key(M, "F10", L.group["dock"].dropdown_toggle("ranger"), desc="SRang"),
    Key(M, "F9", L.group["dock"].dropdown_toggle("sysmon"), desc="SSys"),
    Key(M, "c", L.group["scratch"].dropdown_toggle("chatbot"), desc="Chat"),
    Key(M, "n", L.group["scratch"].dropdown_toggle("note"), desc="Note"),
    Key(M, "p", L.group["scratch"].dropdown_toggle("keepassxc"), desc="Keep"),
    KeyChord(
        M,
        "x",
        [],
        name="quicklaunch",
        mode=True,
        desc="Quick",
    ),
    KeyChord(
        M,
        "s",
        [
            Key(
                [],
                "c",
                L.spawn("kitty -T floating -e tmux attach -t MUSIC:cmus"),
                desc="Tmux",
            ),
            Key([], "Right", L.spawn("cmus-remote -n"), desc="Next"),
            Key(C, "Right", L.spawn("next_album.xsh"), desc="NAlb"),
            Key([], "Left", L.spawn("cmus-remote -r"), desc="Prev"),
            Key([], "space", L.spawn("cmus-remote -u"), desc="Play"),
            Key(
                [],
                "s",
                L.spawn(["alacritty", "-T", "floating", "-e", "fzf_songlauncher.sh"]),
                desc="Song",
            ),
            Key(
                [],
                "a",
                L.spawn("alacritty -T floating -e fzf_albumlauncher.xsh"),
                desc="Alb",
            ),
            Key([], "r", L.spawn("random_album.xsh"), desc="Rand"),
            Key([], "p", L.spawn("playlist_player.xsh"), desc="Plst"),
            Key(A, "p", L.spawn("playlist_randomizer.xsh"), desc="PlRnd"),
        ],
        name="cmus",
        mode=True,
        desc="Music",
    ),
    KeyChord(
        M,
        "F1",
        [
            Key([], "k", L.spawn("keyboard-help.sh"), desc="Keymap"),
            Key([], "q", L.ungrab_all_chords(), desc="Exit"),
        ],
        name="help",
        mode=True,
        desc="Help",
    ),
]

# Mouse (already uses standard modifiers and format)
mouse = [
    Drag(
        M,  # Uses the defined M list
        "Button1",
        L.window.set_position_floating(),
        start=L.window.get_position(),
    ),
    Drag(
        M,  # Uses the defined M list
        "Button3",
        L.window.set_size_floating(),
        start=L.window.get_size(),
    ),
    Click(M, "Button2", L.window.bring_to_front()),  # Uses the defined M list
]

# Groups (Convert the loop that adds group keys)
for g in "123456":
    keys.extend(
        [
            # EzKey(f"M-{g}", ...) -> Key(M, g, ...)
            Key(M, g, L.group[g].toscreen(toggle=True), desc=f"G{g}"),
            # EzKey(f"M-S-{g}", ...) -> Key(M + S, g, ...)
            Key(M + S, g, L.window.togroup(g), desc=f"To{g}"),
        ]
    )
