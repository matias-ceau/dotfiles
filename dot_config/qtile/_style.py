from dataclasses import dataclass


@dataclass
class Colors:
    BASE_100 = "#dad8ce"
    BASE_150 = "#cecdc3"
    BASE_200 = "#b7b5ac"
    BASE_300 = "#979592"
    BASE_50 = "#e6e4d9"
    BASE_500 = "#878580"
    BASE_600 = "#6f6e69"
    BASE_700 = "#575653"
    BASE_800 = "#403e3c"
    BASE_850 = "#343331"
    BASE_900 = "#282726"
    BASE_950 = "#1c1b1a"
    BLACK = "#100f0f"
    BLUE_400 = "#4385be"
    BLUE_600 = "#205ea6"
    CYAN_400 = "#3aa99f"
    CYAN_50 = "#ebf2e7"
    CYAN_600 = "#24837b"
    CYAN_950 = "#142625"
    GREEN_400 = "#879a39"
    GREEN_600 = "#66800b"
    MAGENTA_400 = "#ce5d97"
    MAGENTA_600 = "#a02f6f"
    ORANGE_400 = "#da702c"
    ORANGE_600 = "#bc5215"
    PURPLE_400 = "#8b7ec8"
    PURPLE_600 = "#5e409d"
    RED_400 = "#d14d41"
    RED_600 = "#af3029"
    TRUEBLACK = "#ffffff"
    YELLOW_100 = "#fceeb8"
    YELLOW_400 = "#d0a215"
    YELLOW_600 = "#ad8301"
    YELLOW_900 = "#4d3a0b"


@dataclass
class UIColors:
    accent = [Colors.YELLOW_400]
    black = [Colors.BASE_950]
    groupbox_inactive = [Colors.BASE_300]
    groupbox_block = [Colors.BLACK]
    chord_quick = [Colors.GREEN_400, Colors.BASE_900]
    chord_cmus = [Colors.YELLOW_400, Colors.BASE_900]
    cmus_noplay = [Colors.BASE_300]
    cmus_play = [
        Colors.YELLOW_400,
    ]
    window_name = [
        Colors.BASE_950,
    ]
    net = [
        Colors.BASE_300,
    ]
    volume = [
        Colors.MAGENTA_400,
    ]
    cameleon = [
        Colors.YELLOW_400,
    ]
    cpu_temp = [
        Colors.RED_400,
    ]
    cpu_load = [
        Colors.ORANGE_400,
    ]
    RAM = [
        Colors.BASE_300,
    ]
    systray = [
        Colors.BASE_900,
    ]
    clock = [
        Colors.YELLOW_100,
        Colors.BASE_900,
    ]
    bar_background = [
        Colors.BASE_950,
    ]


widget_defaults = dict(
    font="Iosevka Nerd Font",
    fontsize=14,
    padding=1,
)

extension_defaults = widget_defaults.copy()
