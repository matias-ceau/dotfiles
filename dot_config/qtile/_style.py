## Configuration
widget_defaults = dict(
    font="Iosevka Nerd Font",
    fontsize=12,
    padding=1,
)


extension_defaults = widget_defaults.copy()

colors = dict(
    accent="#d79921",  # Muted yellow for accent, similar to highlighted text
    black="#181818",  # Very dark gray, almost black for background
    groupbox_inactive="#959798",  # Dark grayish-brown for inactive elements
    # groupbox_decoration = "#83a598",  # Slightly darker shade for decorations
    groupbox_block="#000000",
    chord_quick=("#98971a", "#282828"),  # Muted green on dark background
    chord_cmus=("#d79921", "#282828"),  # Muted yellow on dark background
    cmus_noplay="#a89984",  # Light grayish-brown for inactive elements
    cmus_play="#b8bb26",  # Brighter green for active elements
    window_name="#1d2021",  # Muted blue for window names
    net="#8ec07c",  # Muted aqua for network info
    volume="#d3869b",  # Muted purple for volume
    cameleon="#fabd2f",  # Brighter yellow for dynamic elements
    cpu_temp="#fb4934",  # Muted red for temperature
    cpu_load="#fe8019",  # Muted orange for CPU load
    RAM="#8ec07c",  # Muted aqua for RAM (same as net)
    systray="#282828",  # Dark background for system tray
    clock=("#ebdbb2", "#282828"),  # Light text on dark background for clock
    bar_background="#1d2021",  # Slightly darker than main background for bar
)
