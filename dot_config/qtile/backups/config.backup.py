import os, subprocess
from libqtile.log_utils import logger
from libqtile import hook
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

@hook.subscribe.startup_once
def autostart():
    subprocess.call('sh '+os.path.expanduser('~/.config/qtile/autostart.sh'), shell=True)

mod = "mod4"
terminal = 'urxvt'#guess_terminal()

# ----------- CMD DICTS ---------------------------------------------------------------------------------------
#SCRIPTS
script_dict = {'xonsh' : '.xsh', 'sh' : '.sh', 'python3': '.py'}
SCRIPTS = dict()
for i in os.listdir('/home/matias/scripts'):
    for c, e in script_dict.items():
        if '.'+i.split('.')[-1] == e:
            SCRIPTS[i.split('.')[0]] = f"{c} /home/matias/scripts/{i}"

#QUICKLAUNCHES
#jupyter
notebooks = [n[:-6] for n in os.listdir('/home/matias/projects') if n[-6:] == '.ipynb']
nb_commands = [f"jupyter-notebook --browser=chromium /home/matias/projects/{n}.ipynb" for n in notebooks]
NOTEBOOKS = {k:v for k,v in zip(notebooks, nb_commands)}

# -------------------------------------------------------------------------------------------------------------

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod,'shift'], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key( [mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "Up", lazy.next_screen()),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.spawn('dmenu_run -l 30'), desc="Run app with dmenu"),

    # Window commands
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating",),
    Key([mod], "m", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen",),

    #quicklaunch 
    KeyChord([mod], "w", 
        [
        Key([],'n', lazy.run_extension(extension.CommandSet(commands=NOTEBOOKS, dmenu_lines=30))),
        Key(['shift'],'n', lazy.spawn('xonsh /home/matias/scripts/jupyter_new_notebook.xsh'), desc='Launch new notebook'),
        ], mode='quicklaunch'),
    #scripts
    Key([mod], 'x', lazy.run_extension(extension.CommandSet(
        commands=SCRIPTS, dmenu_lines=30, pre_commands=[]))),
    #CMUS
    #TODO add seek etc
    KeyChord([mod], 'c',
        [
        Key([],'c',  lazy.spawn('urxvt -e tmux new -A -s music -n cmus cmus'), desc='start/attach tmux'),
        Key([],'Right', lazy.spawn('cmus-remote -n'), desc='next song'),
        Key(['control'],'Right', lazy.spawn('xonsh /home/matias/scripts/next_album.xsh'), desc='Next album'),
        Key([],'Left',  lazy.spawn('cmus-remote -r'), desc='previous song'),
        Key([],'space',  lazy.spawn('cmus-remote -u'), desc='play/pause'),
        Key([],'s',  lazy.spawn('urxvt -e sh /home/matias/scripts/fzf_songlauncher.sh'), desc='select song'),
        Key([],'a',  lazy.spawn('urxvt -e sh /home/matias/scripts/fzf_albumlauncher.sh'), desc='select song'),
        Key([],'r',  lazy.spawn('xonsh /home/matias/scripts/random_album.xsh'), desc='select random album'),
        Key([], 'p', lazy.spawn('xonsh /home/matias/scripts/playlist_player.xsh'), desc='play playlist'),
        Key(['mod1'], 'p', lazy.spawn('xonsh /home/matias/scripts/playlist_randomizer.xsh'), desc='play playlist in random order'),
        ], mode='cmus'),
        #commands={
        #    'play/pause' : 'cmus-remote -u',
        #    'next'       : 'cmus-remote -n',
        #    'previous'   : 'cmus-remote -r',
        #    'repeat'     : 'cmus-remote -R',
        #    'shuffle'    : 'cmus-remote -S',
        #    'start'      : 'urxvt -e tmux new -s music -n cmus cmus' },
        #dmenu_command='dmenu -l 30', pre_commands=[]))),
]

groups = [
        Group('a', label='a'),
        Group('z', label='z'),
        Group('e', label='e'),
        Group('r', label='r'),
        Group('t', label='t'),
        Group('y', label='y'),
         ]

for i in groups:
    keys.extend(
        [
      Key([mod],i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
      Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="move focused window to group {}".format(i.name)),
        ]
    )

groups.append(
    ScratchPad("scratchpad",
        [DropDown("terminal", "urxvt",                   x=0.01, y=0, width=0.98, height=0.8, opacity=0.9, on_focus_lost_hide=False),
         DropDown("vimwiki",  "urxvt -hold -e vim",      x=0.01, y=0, width=0.98, height=0.8, opacity=0.9, on_focus_lost_hide=False),
         DropDown("ranger",   "urxvt -hold -e ranger",   x=0.01, y=0, width=0.98, height=0.8, opacity=0.9, on_focus_lost_hide=False),
         DropDown("ipython",  "urxvt -hold -e 'ipython'",x=0.01, y=0, width=0.98, height=0.8, opacity=0.9, on_focus_lost_hide=False),
         DropDown("browser",  "urxvt -hold -e lynx",     x=0.01, y=0, width=0.98, height=0.8, opacity=0.9, on_focus_lost_hide=False)])
        )

keys.extend([
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('terminal')),
    Key([], 'F11', lazy.group['scratchpad'].dropdown_toggle('vimwiki')),
    Key([], 'F10', lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key([], 'F9',  lazy.group['scratchpad'].dropdown_toggle('ipython')),
    Key([], 'F8',  lazy.group['scratchpad'].dropdown_toggle('browser')),
    Key([], 'F1', lazy.spawn('xonsh /home/matias/scripts/karjala_screen.xsh'), desc='Screen setup')
    ])

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    layout.Bsp(),
    layout.Matrix(),
    layout.MonadTall(),
    layout.MonadWide(),
    layout.RatioTile(),
    layout.Tile(),
    layout.TreeTab(),
    layout.VerticalTile(),
    layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentScreen(),
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={ "launch": ("#ff0000", "#ffffff"), }, name_transform=lambda name: name.upper(),),
                widget.NvidiaSensors(),
                widget.ThermalSensor(),
                widget.DF(visible_on_warn=False),
                widget.CPU(),
                widget.Memory(measure_mem='G'),
                widget.Net(),
                widget.Systray(),
                widget.Clipboard(),
                widget.Clock(format="%Y-%m-%d %a %H:%M"),
                widget.QuickExit(),
            ],
            24,
            border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                    ),
        wallpaper='~/pictures/wallpapers/0.jpg',
        wallpaper_mode='fill'
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentScreen(),
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.CheckUpdates(),
                widget.Cmus(),
                widget.WidgetBox(widgets=[
                    widget.CPUGraph(),
                    widget.MemoryGraph()]),
                widget.Chord(
                    chords_colors={ "launch": ("#ff0000", "#ffffff"), }, name_transform=lambda name: name.upper(),),
                widget.Clock(format="%Y-%m-%d %a %H:%M"),
            ],
            24,
                    ),
        wallpaper='~/pictures/wallpapers/0.jpg',
        wallpaper_mode='fill'
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
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
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = False#True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

