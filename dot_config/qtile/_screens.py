from _custom import Cameleon, custom_args, scale, system_clock_args
from _style import Colors as C
from _style import UIColors as UI
from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

# from qtile_extras import widget

# ------ SCREEN AND BAR DEFINITION ---------------------------------------------
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="\u2630", mouse_callbacks={"Button1": lazy.spawn("jgmenu_run")}
                ),
                # Current screen
                widget.CurrentScreen(active_text="\u2022", inactive_text="\u2022"),
                # Groupbox
                widget.GroupBox(
                    highlight_method="block",
                    disable_drag=True,
                    inactive=UI.groupbox_inactive,
                    this_current_screen_border=UI.groupbox_block,
                    this_screen_border=UI.groupbox_block,
                ),
                # Current Layout icon
                widget.CurrentLayoutIcon(use_mask=True, scale=0.9),
                # Chords
                widget.Chord(
                    chords_colors={
                        "quicklaunch": UI.chord_quick,
                        "cmus": UI.chord_cmus,
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # Window name
                widget.WindowName(
                    # foreground=colors['window_name'],
                ),
                # CMUS (inactive)
                widget.Cmus(
                    format="{play_icon}{artist} - {title} {album}",
                    noplay_color=UI.cmus_noplay,
                    play_colour=UI.cmus_play,
                    dpi=96,
                    width=int(400 * scale),
                    scroll=True,
                    scroll_fixed_width=True,
                ),
                # Net
                widget.Net(
                    format="{down:>4.0f}{down_suffix:<2} ↓↑{up:>4.0f}{up_suffix:<2}",
                    width=100,
                    scroll=True,
                    scroll_fixed_width=True,
                    foreground=UI.net,
                ),
                # Volume
                widget.Volume(
                    unmute_format="\U0001f508\u3014 {volume:>2} \u3015",
                    mute_format="\U0001f507  ",
                    mouse_callbacks={
                        "Button3": lazy.spawn("amixer -q set Master toggle")
                    },
                    foreground=UI.volume,
                ),
                # Cameleon
                Cameleon(foreground=UI.cameleon, **custom_args),
                widget.TunedManager(),
                # genPoll
                # Thermal Sensor CPU
                widget.ThermalSensor(
                    format="{temp:.0f}\u2103 ",
                    tag_sensor="Package id 0",
                    width=50,
                    padding=0,
                    foreground=UI.cpu_temp,
                ),
                # CPU load
                widget.CPU(
                    format="{freq_current}\u3393  {load_percent}%",
                    scroll=True,
                    scroll_fixed_width=True,
                    width=100,
                    padding=0,
                    foreground=UI.cpu_temp,
                ),
                # Storage (DF)
                widget.DF(
                    format=" {uf:3} ",
                    visible_on_warn=False,
                    partition="/",
                ),
                widget.Memory(measure_mem="G", foreground=UI.RAM),
                # widget.Systray( foreground=UI.systray,),
                # widget.Tuned
                widget.StatusNotifier(),
                widget.Clock(
                    **system_clock_args,
                    fmt="<b>\u3014 {} \u3015</b>",
                    foreground=UI.clock[0],
                    background=UI.clock[1],
                ),
                widget.QuickExit(default_text="\u23cf"),
            ],
            20,  # ?
            border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            border_color=[
                C.BLACK,
                C.BLACK,
                C.ORANGE_400,
                C.BLACK,
            ],
            background=UI.bar_background,
        ),
    )
]
