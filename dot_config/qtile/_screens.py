from _style import colors, powerline_1, decoration_group, extension_defaults, widget_defaults
from _custom import Cameleon, custom_args, system_clock_args, scale
from libqtile.config import Screen
from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget


#------ SCREEN AND BAR DEFINITION ---------------------------------------------
screens = [
    Screen(
        top=bar.Bar(
            [
            widget.TextBox(
                text='\u2630',
                mouse_callbacks={'Button1': lazy.spawn("jgmenu_run")}
                ),

            # Current screen
            widget.CurrentScreen(
            active_text="\u2022", inactive_text="\u2022"),

            # Groupbox
            widget.GroupBox(
                highlight_method="block",
                disable_drag=True,
                inactive=colors['groupbox_inactive'],
                **decoration_group,
                ),

            # Current Layout icon
            widget.CurrentLayoutIcon(use_mask=True,
                                      scale=0.9,
                                      **powerline_1),

            # Chords
            widget.Chord(
                 chords_colors={
                     "quicklaunch": colors['chord_quick'],
                     "cmus": colors['chord_cmus'],
                 },
                 name_transform=lambda name: name.upper(),
                 ),

            # Window name
            widget.WindowName(
                #foreground=colors['window_name'],
                ),

            # CMUS (inactive)
            widget.Cmus(
                format="{play_icon}{artist} - {title} {album}",
                noplay_color=colors['cmus_noplay'],
                play_colour=colors['cmus_play'],
                dpi=96,
                width=int(400 * scale),
                scroll=True,
                scroll_fixed_width=True,
            ),

            # Net
            widget.Net(
                format="{down:4.0f}{down_suffix:<2} ↓↑{up:4.0f}{up_suffix:<2}",
                width = 90,
                scroll =True,
                scroll_fixed_width=True,
                foreground=colors['net'],
                **powerline_1
            ),

            # Volume
            widget.Volume(
                unmute_format="\U0001f508\u3014 {volume:>2} \u3015",
                mute_format="\U0001f507  ",
                mouse_callbacks={
                    "Button3": lazy.spawn("amixer -q set Master toggle")
                },
                foreground=colors['volume'],
                **powerline_1
            ),

            # Cameleon
            Cameleon(foreground=colors['cameleon'],
                     **custom_args,
                     **powerline_1),

            # Thermal Sensor CPU
            widget.ThermalSensor(
                    format="\u2102\u3014 {temp:.0f}\u2103 ",
                    tag_sensor="Package id 0",
                    width=55,
                    padding=0,
                    foreground=colors['cpu_temp'],
                    **powerline_1,
                    ),

            # CPU load
            widget.CPU(format="{freq_current}\u3393  {load_percent}% \u3015", 
                       scroll=True,
                       scroll_fixed_width=True,
                       width=85,
                       padding=0,
                       foreground=colors['cpu_temp'],
                       ),

            # Storage (DF)
            widget.DF(format="\u3014 {uf:3} \u3015", 
                      visible_on_warn=False, 
                      partition="/",
                      **powerline_1),

            widget.Memory(measure_mem="G", 
                          foreground=colors['RAM'],
                          **powerline_1),

            widget.Systray(foreground=colors['systray'], **powerline_1),

            widget.Clock(
                **system_clock_args,
                fmt="<b>\u3014 {} \u3015</b>",
                foreground=colors['clock'][0],
                background=colors['clock'][1],
                **powerline_1
            ),

            widget.QuickExit(default_text="\u23cf"),
            ],

            20,  # ?

            border_width=[1, 0, 1, 0],  # Draw top and bottom borders

            border_color=[colors['accent'],
                           colors['black'],
                           colors['accent'],
                           colors['black']
                           ],  # Borders are magenta

            background=colors['bar_background'],
        ),
    )
]

