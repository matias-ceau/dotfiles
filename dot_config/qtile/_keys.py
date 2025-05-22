from libqtile import extension
from libqtile.config import Click, Drag, EzKey, EzKeyChord
from libqtile.lazy import lazy as L

# M = ["mod4"]
# A = ["mod1"]
# S = ["shift"]
# C = ["control"]
brightnessdown, brightnessup = "XF86MonBrightnessDown", "XF86MonBrightnessUp"
volumedown, volumeup, mute = (
    "XF86AudioLowerVolume",
    "XF86AudioRaiseVolume",
    "XF86AudioMute",
)
forward, back = "XF86Forward", "XF86Back"

keys = [
    # Navigation
    EzKey("M-A-Home", L.next_screen(), desc="NextScr"),
    EzKey("M-h", L.layout.left(), desc="Left"),
    EzKey("M-l", L.layout.right(), desc="Right"),
    EzKey("M-j", L.layout.down(), desc="Down"),
    EzKey("M-k", L.layout.up(), desc="Up"),
    EzKey("M-Tab", L.layout.next(), desc="NextPane"),
    EzKey("M-A-j", L.group.next_window(), desc="NextWin"),
    EzKey("M-A-k", L.group.prev_window(), desc="PrevWin"),
    EzKey(
        "M-S-bracketright",
        L.spawn("qtile_window_to_group_and_switch.py -n"),
        desc="NextGrp",
    ),
    EzKey(
        "M-S-bracketleft",
        L.spawn("qtile_window_to_group_and_switch.py -p"),
        desc="PrevGrp",
    ),
    EzKey("M-Right", L.screen.next_group(), desc="NextGrp"),
    EzKey("M-bracketright", L.screen.next_group(), desc="NextGrp"),
    EzKey("M-Left", L.screen.prev_group(), desc="PrevGrp"),
    EzKey("M-bracketleft", L.screen.prev_group(), desc="PrevGrp"),
    EzKey("M-C-A-grave", L.next_layout(), desc="NextLay"),
    EzKey("M-C-A-1", L.to_layout_index(0), desc="Lay1"),
    EzKey("M-C-A-2", L.to_layout_index(1), desc="Lay2"),
    EzKey("M-C-A-3", L.to_layout_index(2), desc="Lay3"),
    EzKey("M-C-A-4", L.to_layout_index(3), desc="Lay4"),
    EzKey("M-C-A-5", L.to_layout_index(4), desc="Lay5"),
    EzKey("M-C-A-6", L.to_layout_index(5), desc="Lay6"),
    EzKey("M-q", L.window.kill(), desc="Kill"),
    EzKey("M-C-r", L.reload_config(), desc="Reload"),
    EzKey("M-C-S-r", L.restart(), desc="Restart"),
    EzKey("M-A-q", L.shutown(), desc="Shutdown"),
    # EzKey("M-C-q", L.function(show_power_menu), desc="Power"), # Uncomment if needed
    # EzKey("M-w", L.run_extension(extension.WindowList()), desc="WinList"),
    # Move
    EzKey("M-S-h", L.layout.shuffle_left(), desc="MvLeft"),
    EzKey("M-S-l", L.layout.shuffle_right(), desc="MvRight"),
    EzKey("M-S-j", L.layout.shuffle_down(), desc="MvDown"),
    EzKey("M-S-k", L.layout.shuffle_up(), desc="MvUp"),
    # Resize
    EzKey("M-C-h", L.layout.grow_left(), desc="GrLeft"),
    EzKey("M-C-l", L.layout.grow_right(), desc="GrRight"),
    EzKey("M-C-j", L.layout.grow_down(), desc="GrDown"),
    EzKey("M-C-k", L.layout.grow_up(), desc="GrUp"),
    EzKey("M-C-equal", L.layout.normalize(), desc="Norm"),
    # Floating
    EzKey(
        "M-minus",
        L.window.resize_floating(-60, -40).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Float-",
    ),
    EzKey(
        "M-S-minus",
        L.window.resize_floating(-15, -10).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Float--",
    ),
    EzKey(
        "M-equal",
        L.window.resize_floating(60, 40).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Float+",
    ),
    EzKey(
        "M-S-equal",
        L.window.resize_floating(15, 10).when(when_floating=True),
        L.window.center().when(when_floating=True),
        desc="Float++",
    ),
    EzKey("M-Prior", L.layout.toggle_split(), desc="Split"),
    EzKey("M-f", L.window.toggle_floating(), desc="Float"),
    EzKey("M-m", L.window.toggle_fullscreen(), desc="Full"),
    EzKey("M-Up", L.screen.toggle_group(), desc="LastGrp"),
    # Media / function keys
    EzKey("<XF86MonBrightnessUp>", L.spawn("light -A 10"), desc="Bri+"),
    EzKey("<XF86MonBrightnessDown>", L.spawn("light -U 10"), desc="Bri-"),
    EzKey("<XF86AudioMute>", L.spawn("amixer -q set Master toggle"), desc="Mute"),
    EzKey("<XF86AudioLowerVolume>", L.widget["volume"].decrease_vol(), desc="Vol-"),
    EzKey("<XF86AudioRaiseVolume>", L.widget["volume"].increase_vol(), desc="Vol+"),
    EzKey("M-S-F2", L.spawn("wallpaper.sh --select"), desc="Wall"),
    # Commands
    EzKey("M-S-d", L.spawn("dmenu_run -l 30"), desc="Dmenu"),
    EzKey("M-space", L.spawn("fzfmenu_run.sh"), desc="Fzf"),
    EzKey("M-S-space", L.spawn("fuzzel"), desc="Rofi"),
    EzKey("M-semicolon", L.spawn("script_launcher.sh"), desc="Script"),
    EzKey("M-Return", L.spawn(["kitty", "-1"]), desc="Term"),
    EzKey("M-S-t", L.spawn(["alacritty", "-T", "dis_term"]), desc="Term2"),
    EzKey("M-t", L.spawn(["alacritty", "-T", "floating"]), desc="Tfloat"),
    EzKey("M-S-o", L.spawn("obsidian-vault-selector.sh"), desc="Obs"),
    EzKey("M-o", L.spawn("qutebrowser"), desc="Qute"),
    EzKey("M-b", L.spawn("opera"), desc="Opera"),
    EzKey("M-Print", L.spawn("screenshot"), desc="Shot"),
    EzKey("M-C-Print", L.spawn("screenshot --select"), desc="ShotSel"),
    EzKey("M-A-Print", L.spawn("ocrdesktop"), desc="OCR"),
    # Scratchpads
    EzKey("F12", L.group["dock"].dropdown_toggle("terminal"), desc="STerm"),
    EzKey("M-F11", L.group["dock"].dropdown_toggle("nvim"), desc="SNvim"),
    EzKey("M-F10", L.group["dock"].dropdown_toggle("ranger"), desc="SRang"),
    EzKey("M-F9", L.group["dock"].dropdown_toggle("sysmon"), desc="SSys"),
    EzKey("M-c", L.group["scratch"].dropdown_toggle("chatbot"), desc="Chat"),
    EzKey("M-n", L.group["scratch"].dropdown_toggle("note"), desc="Note"),
    EzKey("M-p", L.group["scratch"].dropdown_toggle("keepassxc"), desc="Keep"),
    # EzKeyChord examples
    EzKeyChord(
        "M-x",
        [
            # EzKey("S-n", L.spawn("jupyter_new_notebook.xsh"), desc="NewNb"),
        ],
        name="quicklaunch",
        mode=True,
        desc="Quick",
    ),
    EzKeyChord(
        "M-s",
        [
            EzKey(
                "c",
                L.spawn("kitty -T floating -e tmux attach -t MUSIC:cmus"),
                desc="Tmux",
            ),
            EzKey("Right", L.spawn("cmus-remote -n"), desc="Next"),
            EzKey("C-Right", L.spawn("next_album.xsh"), desc="NAlb"),
            EzKey("Left", L.spawn("cmus-remote -r"), desc="Prev"),
            EzKey("space", L.spawn("cmus-remote -u"), desc="Play"),
            EzKey(
                "s",
                L.spawn(["alacritty", "-T", "floating", "-e", "fzf_songlauncher.sh"]),
                desc="Song",
            ),
            EzKey(
                "a",
                L.spawn("alacritty -T floating -e fzf_albumlauncher.xsh"),
                desc="Alb",
            ),
            EzKey("r", L.spawn("random_album.xsh"), desc="Rand"),
            EzKey("p", L.spawn("playlist_player.xsh"), desc="Plst"),
            EzKey("A-p", L.spawn("playlist_randomizer.xsh"), desc="PlRnd"),
        ],
        name="cmus",
        mode=True,
        desc="Music",
    ),
    EzKeyChord(
        "M-F1",
        [
            EzKey("k", L.spawn("keyboard-help.sh"), desc="Keymap"),
            EzKey("q", L.ungrab_all_chords(), desc="Exit"),
        ],
        name="help",
        mode=True,
        desc="Help",
    ),
]

# Mouse
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

# Groups
for g in "123456":
    keys.extend(
        [
            EzKey(f"M-{g}", L.group[g].toscreen(toggle=True), desc=f"G{g}"),
            EzKey(f"M-S-{g}", L.window.togroup(g), desc=f"To{g}"),
        ]
    )
