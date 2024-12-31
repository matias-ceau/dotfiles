from _colors import Colors as c

widget_defaults = dict(
    font="Iosevka Nerd Font",
    fontsize=12,
    padding=1,
)

extension_defaults = widget_defaults.copy()

colors = dict(
    accent=c.yellow_400,  # Muted yellow for accent, similar to highlighted text
    black=c.base_950,  # Very dark gray, almost black for background
    groupbox_inactive=c.base_300,  # Dark grayish-brown for inactive elements
    # groupbox_decoration = c.base_300,  # Slightly darker shade for decorations
    groupbox_block=c.black,
    chord_quick=(c.green_400, c.base_900),  # Muted green on dark background
    chord_cmus=(c.yellow_400, c.base_900),  # Muted yellow on dark background
    cmus_noplay=c.base_300,  # Light grayish-brown for inactive elements
    cmus_play=c.yellow_400,  # Brighter green for active elements
    window_name=c.base_950,  # Muted blue for window names
    net=c.base_300,  # Muted aqua for network info
    volume=c.magenta_400,  # Muted purple for volume
    cameleon=c.yellow_400,  # Brighter yellow for dynamic elements
    cpu_temp=c.red_400,  # Muted red for temperature
    cpu_load=c.orange_400,  # Muted orange for CPU load
    RAM=c.base_300,  # Muted aqua for RAM (same as net)
    systray=c.base_900,  # Dark background for system tray
    clock=(c.yellow_100, c.base_900),  # Light text on dark background for clock
    bar_background=c.base_950,  # Slightly darker than main background for bar
)
