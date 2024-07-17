from __future__ import annotations
import os
import subprocess
import socket

# from libqtile.log_utils import logger
from libqtile import hook
from libqtile import bar, layout, extension #widget, 
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
    ScratchPad,
    DropDown,
    KeyChord,
)
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

from qtile_extras import widget

hostname = socket.gethostname()
home = os.path.expanduser("~")
scripts = home + "/.scripts"


@hook.subscribe.startup_once
def autostart():
    auto = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([auto])

mod = "mod4"

terminal = "kitty"
# terminal = 'urxvt'#guess_terminal()
# terminal = 'alacritty'

# HOST SPECIFIC
scale = 1.0
if hostname == "karhu":
    scale = 0.5

# ----------- CMD DICTS ---------------------------------------------------------------------------------------
# TODO create scripts for these 2
# SCRIPTS
script_dict = {"xonsh": ".xsh", "sh": ".sh", "python3": ".py"}
SCRIPTS = dict()
for i in os.listdir(f"{home}/apps/scripts"):
    for c, e in script_dict.items():
        if "." + i.split(".")[-1] == e:
            SCRIPTS[i.split(".")[0]] = f"{c} {home}/apps/scripts/{i}"

# def launch_user_script():
#    SCRIPT = {}
#    for i in

# QUICKLAUNCHES
# jupyter
notebooks = [n[:-6] for n in os.listdir(f"{home}/projects") if n[-6:] == ".ipynb"]
nb_commands = [
    f"jupyter-notebook --browser=chromium {home}/projects/{n}.ipynb" for n in notebooks
]
NOTEBOOKS = {k: v for k, v in zip(notebooks, nb_commands)}

# -------------------------------------------------------------------------------------------------------------

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window",
    ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "control"], "equal", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "Prior", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Tab", lazy.screen.next_group(), desc="Cycle groups"),
    Key([mod], "BackSpace", lazy.screen.prev_group(), desc="Cycle groups"),
    Key([mod], "twosuperior", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "control"], "Home", lazy.next_screen(), desc="Go to next screen"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "w", lazy.run_extension(extension.WindowList()), desc="List all windows"),
    # Window commands
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating",),
    Key( [mod], "m", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen",),
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),
    # wpctl set-volume -l 1.5 @DEFAULT_AUDIO_SINK@ 5%+ ### amixer -D pulse sset Master 5%+
    # wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-        ### amixer -D pulse sset Master 5%-
    # wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle     ### amixer sset Master toggle

    # Key([], 'XF86AudioMicMute'
    # Key([], 'XF86Bluetooth'
    # Key([], 'XF86Display'
    # Key([], 'XF86Favorites'
    # Key([], 'XF86Tools'
    Key([mod], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "d", lazy.spawn("dmenu_run -l 30"), desc="Run app with dmenu"),
    Key([mod], "space", lazy.spawn("fzfmenu_run.sh"), desc="Run app with fzfmenu"),
#    Key([mod], "b", lazy.spawn('notify-send "Hello" "hihi"'), desc="bookmarks"),  # TODO (also add, auto format, copy/paste)
    Key([mod], "b", lazy.spawn(["xterm", "-T", "floating", "-e", f"{scripts}/fzf_songlauncher.sh"]), desc="bookmarks"),  # TODO (also add, auto format, copy/paste)
    Key([mod], "Return", lazy.spawn(['kitty','-1']), desc="Launch terminal"),
    Key([mod], "dollar", lazy.spawn(['alacritty','-T','dis_term']), desc="Launch terminal"),
    Key([mod], "o", lazy.spawn("obsidian.xsh"), desc="Open obsidian vault"),
    Key([], "Print", lazy.spawn("flameshot gui")),
    # quicklaunch
    KeyChord(
        [mod], "less", 
            [
              Key([], "n", lazy.run_extension( extension.CommandSet(commands=NOTEBOOKS, dmenu_lines=30)),),
              Key(["shift"], "n", lazy.spawn("jupyter_new_notebook.xsh"), desc="Launch new notebook",),
        ],
        name="quicklaunch",
    ),
    # scripts
    Key(
        [mod], "x",
        lazy.run_extension(extension.CommandSet(commands=SCRIPTS, dmenu_lines=30, pre_commands=[])
        ),
    ),
    # CMUS
    # TODO add seek etc
    KeyChord(
        [mod, "shift"], "c",
        [
            Key([], "c", lazy.spawn("urxvt -T floating -e tmux attach -t music:cmus"),
                desc="attach tmux",),
            Key([], "Right", lazy.spawn("cmus-remote -n"),
                desc="next song"),
            Key(["control"], "Right", lazy.spawn(f"{scripts}/next_album.xsh"),
                desc="Next album",),
            Key([], "Left", lazy.spawn("cmus-remote -r"), 
                desc="previous song"),
            Key([], "space", lazy.spawn("cmus-remote -u"), 
                desc="play/pause"),
            Key([], "s", lazy.spawn( ["xterm", "-T", "floating", "-e", f"{scripts}/fzf_songlauncher.sh"]), 
                desc="select song",),
            Key([], "a", lazy.spawn(f"xterm -T floating -e {scripts}/fzf_albumlauncher.xsh"), 
                desc="select song",),
            Key([], "r", lazy.spawn(f"{scripts}/random_album.xsh"), 
                desc="select random album",),
            Key([], "p", lazy.spawn(f"{scripts}/playlist_player.xsh"),
                desc="play playlist",),
            Key(["mod1"], "p", lazy.spawn(f"{scripts}/playlist_randomizer.xsh"),
                desc="play playlist in random order",),
        ],
        name="cmus",
    ),
    # commands={
    #    'play/pause' : 'cmus-remote -u',
    #    'next'       : 'cmus-remote -n',
    #    'previous'   : 'cmus-remote -r',
    #    'repeat'     : 'cmus-remote -R',
    #    'shuffle'    : 'cmus-remote -S',
    #    'start'      : 'urxvt -e --title "floating" tmux new -s music -n cmus cmus' },
    # dmenu_command='dmenu -l 30', pre_commands=[]))),
]

groups = [
    Group("a", label="\u1d00"),
    Group("z", label="\u1d22"),
    Group("e", label="\u1d07"),
    Group("r", label="\u0280"),
    Group("t", label="\u1d1b"),
    Group("y", label="\u028f"),
]

for g in groups:
    keys.extend(
        [Key([mod], g.name, lazy.group[g.name].toscreen(toggle=True), desc=f"Switch to group {g.name}",),
         Key([mod, "shift"], g.name, lazy.window.togroup(g.name), desc=f"move focused window to group {g.name}",),]
    )

##    # allow mod3+1 through mod3+0 to bind to groups; if you bind your groups
##    # by hand in your config, you don't need to do this.
##    from libqtile.dgroups import simple_key_binder
##
##    dgroups_key_binder = simple_key_binder("mod3")

groups.extend(
    [
        ScratchPad(
            "dock",
            [ DropDown( "terminal", "alacritty",
                    x=0.01, y=0, width=0.98, height=0.8,
                    on_focus_lost_hide=False),
                DropDown( "vimwiki", ["alacritty","--working-directory", f"{home}/notes", "-T", "vimwiki", "-E", "nvim", f"{home}/index.md"],
                    x=0.01, y=0, width=0.98, height=0.8,
                    on_focus_lost_hide=False),
                DropDown( "ranger", "alacritty -e ranger",
                    x=0.01, y=0, width=0.98, height=0.8,
                    on_focus_lost_hide=False),
                DropDown( "sysmon", ["xterm", "-fs", "10", "-e", "btop"],
                    x=0.01, y=0, width=0.98, height=0.8, opacity=1,
                    on_focus_lost_hide=False)
            ],
            single=True,
                   ),
        ScratchPad( "scratch",
            [DropDown("chatbot", ["alacritty", "-e", "aichat"],
                    x=0.2, width=0.6, y=0.2, height=0.6),
            DropDown("note", ["alacritty", "-e", "vim", f"{home}/notes/draft.md"],
                    x=0.2, width=0.6, y=0.2, height=0.6),
             ]
                   )
        ]
    )
             

keys.extend(
    [
        Key([], "F12", lazy.group["dock"].dropdown_toggle("terminal")),
        Key([mod], "F11", lazy.group["dock"].dropdown_toggle("vimwiki")),
        Key([mod], "F10", lazy.group["dock"].dropdown_toggle("ranger")),
        Key([mod], "F9", lazy.group["dock"].dropdown_toggle("sysmon")),
        # Key([mod], 'F8',  lazy.group['dock'].dropdown_toggle('browser')),
        Key([mod], "F7", lazy.spawn("emacsclient -c -a 'emacs'")),
        Key([mod], "F2", lazy.spawn(f"feh --bg-scale --randomize {home}/.wallpapers/"),
            desc="Wallpaper",),
        Key([mod], "c", lazy.group["scratch"].dropdown_toggle("chatbot")),
        Key([mod], "n", lazy.group["scratch"].dropdown_toggle("note")),
    ]
)

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),  # BASIC
    layout.TreeTab(),  # TODO : add auto add_section/sort_sections | section_up/down
    layout.Max(),  # simple full screen
    layout.Matrix(),  # equally spaced +
    layout.MonadTall(),  # 1 big, other small / flip RL / shuffle up down
    layout.MonadThreeCol(),  # same but 3 col (good for widescreen)
    layout.Zoomy(),  #
    #   layout.Stack(num_stacks=2),                                                # like columns but only 2 stacks (toggle with W-S-Ret)
    #    layout.Bsp(),                                                              # default same direction auto, change d manually
    #    layout.MonadWide(),                                                        # up down
    #    layout.RatioTile(),                                                        # can be useful instead of matrix
    #    layout.Tile(),                                                             #
    #    layout.VerticalTile(),                                                     #
]
# ScreenSplit() to think about for big monitor

widget_defaults = dict(
    font="Inconsolata LGC Nerd Fonts Mono",
    fontsize=10,
    padding=2,
)

extension_defaults = widget_defaults.copy()


# SYSTEM SPECIFIC

if hostname == "karhu":
    Cameleon = type("Cameleon", widget.Battery.__bases__, dict(widget.Battery.__dict__))
    custom_args = dict(format="{char} {percent:2.0%} {watt:.0f}W")

    system_clock_args = dict(format="%H%M")

elif hostname == ("karjala") or (hostname == "kukko"):
    Cameleon = type(
        "Cameleon", widget.NvidiaSensors.__bases__, dict(widget.NvidiaSensors.__dict__)
    )
    custom_args = dict(format="GPU {temp}°C", width=60, dpi=96)

    system_clock_args = dict(format="%Y-%m-%d %a %H:%M")

else:
    Cameleon = type("Cameleon", widget.Sep.__bases__, dict(widget.Sep.__dict__))
########################################################################################

###########" WILL BE USED FOR STATUS BAR ###################""
# import sys
# import time
# from datetime import datetime, timedelta, timezone, tzinfo
#
# from libqtile.command.base import expose_command
# from libqtile.log_utils import logger
# from libqtile.widget import base
#
# import pytz
#
# class CustomWidget(base.InLoopPollText):
#    '''Custom widget, a clock at the moment'''
#    defaults = [("format", "%H:%M", "Blabla"),
#                ("update_interval", 1.0, "Update interval in seconds"),
#                ]
#    DELTA = timedelta(seconds=0.5)
#
#    def __init__(self, **config):
#        base.InLoopPollText.__init__(self, **config)
#        self.add_defaults(CustomWidget.defaults)
#        self.timezone = pytz.timezone('US/Central')
#
#    def tick(self):
#        self.update(self.poll())
#        return self.update_interval - time.time() % self.update_interval
#
#    def poll(self):
#        return (datetime.now(timezone.utc).astimezone(self.timezone) + self.DELTA).strftime(self.format)
#
#    @expose_command
#    def update_timezone(self, timezone_as_str):
#        """
#        Use lazy.widget["customwidget"].update_timezone(timezone_as_str)
#        """
#        self.timezone = pytz.timezon(timezone_as_str)
#        self.update(self.poll())
###############################################################################"
# TODO https://qtile-extras.readthedocs.io/en/stable/manual/ref/decorations.html#powerlinedecoration
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentScreen(active_text="\u2022", inactive_text="\u2022"),
                widget.GroupBox(
                    highlight_method="block", disable_drag=True, inactive="#777777"
                ),
                #widget.CurrentLayout( background="#550055", foreground="#ffffff", width=70, dpi=96),
                widget.CurrentLayoutIcon(use_mask=True,scale=0.9),
                widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        "quicklaunch": ("#00ff00", "#000000"),
                        "cmus": ("#ffff00", "#000000"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.WindowName(),
                #########################
                # widget.WidgetBox(widgets=[
                #    widget.CPUGraph(),
                #    widget.MemoryGraph()]),
                widget.Cmus(
                    format="{play_icon}{artist} - {title} {album}",
                    noplay_color="#cecece",
                    play_colour="#00ff00",
                    dpi=96,
                    width=int(400 * scale),
                    scroll=True,
                    scroll_fixed_width=True,
                ),  # CMUS
                # widget.Pomodoro(scroll=True,width=100,scroll_fixed_width=True),
                widget.Net(
                    format="{down:6.2f}{down_suffix:<2} ↓↑{up:6.2f}{up_suffix:<2}"
                ),
                widget.Sep(padding=4),
                widget.Volume(
                    unmute_format="\U0001f508{volume:>3}",
                    mute_format="\U0001f507  ",
                    mouse_callbacks={
                        "Button3": lazy.spawn("amixer -q set Master toggle"),
                    },
                ),  # VOLUME
                # CustomWidget(),
                Cameleon(**custom_args),
                widget.ThermalSensor(format="CPU {temp:.0f}{unit}", width=60, dpi=96),
                widget.CPU(format="{load_percent:>4}%", padding=5),
                widget.Sep(padding=4),
                widget.DF(format="{uf:>3}", visible_on_warn=False, partition="/"),
                widget.DF(
                    format="{uf:>3}", visible_on_warn=False, partition="/mnt/SSD"
                ),
                widget.DF(
                    format="{uf:>4}", visible_on_warn=False, partition="/mnt/HDD2"
                ),
                widget.DF(
                    format="{uf:>3}", visible_on_warn=False, partition="/mnt/HDD"
                ),
                widget.Sep(padding=4),
                widget.Memory(measure_mem="G"),
                widget.Sep(padding=4),
                # widget.Notify(scroll=True,width=100,scroll_fixed_width=True),
                #widget.StatusNotifier(icon_theme="papyrus"),
                widget.Systray(background="#000000", foreground='#000000'),
                widget.Clock(
                    **system_clock_args,
                    fmt="<b>{}</b>",
                    foreground="#000000",
                    background="#cccccc",
                ),
                widget.QuickExit(default_text="\u274c"),
            ],
            24, #?
            border_width=[1, 0, 1, 0],  # Draw top and bottom borders
            border_color=[
                "#ff00ff",
                "#000000",
                "#ff00ff",
                "#000000",
            ],  # Borders are magenta
            background="#000000",
        ),
#        wallpaper="~/.wallpapers/0.jpg",
#        wallpaper_mode="fill",
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="qjackctl"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="fzfmenu"),
        Match(title="floating"),
    ]
)
auto_fullscreen = False  # True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False  # True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# 2024-06-26 10:55
