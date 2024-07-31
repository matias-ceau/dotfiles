import os
import csv
import socket
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.popup.toolkit import (
        PopupRelativeLayout,
        PopupImage,
        PopupText)

hostname = socket.gethostname()
home = os.path.expanduser("~")
scripts = os.environ.get('SCRIPTS')
script_dict = {"xonsh": ".xsh", "sh": ".sh", "python3": ".py"}

# HOST SPECIFIC
scale = 1.0
if hostname == "karhu":
    scale = 0.5

# ----- CMD DICTS / SPECIAL -----(to be modified)----------------------------------------
# SCRIPTS
def csv_to_dict(file_path):
    result = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            result[row['file']] = os.path.expanduser(f"~/{row['file']}")
    return result

SCRIPTS = csv_to_dict(f'{scripts}/data/script_info.csv')

# QUICKLAUNCHES
# jupyter
notebooks = [n[:-6] for n in os.listdir(f"{home}/projects") if n[-6:] == ".ipynb"]
nb_commands = [
    f"jupyter-notebook --browser=chromium {home}/projects/{n}.ipynb" for n in notebooks
]
NOTEBOOKS = {k: v for k, v in zip(notebooks, nb_commands)}

## Cameleon widget
if (hostname == "karhu") or (hostname == "korvapuusti"):
    Cameleon = type("Cameleon", widget.Battery.__bases__, dict(widget.Battery.__dict__))
    custom_args = dict(format="{char} {percent:2.0%} {watt:.0f}\u1d21")

    system_clock_args = dict(format="%H%M")

elif (hostname == "karjala") or (hostname == "kukko"):
    Cameleon = type(
        "Cameleon", widget.NvidiaSensors.__bases__, dict(widget.NvidiaSensors.__dict__)
    )
    custom_args = dict(format="GPU {temp}°C", width=60, dpi=96)

    system_clock_args = dict(format="%Y-%m-%d %a %H:%M")

else:
    Cameleon = type("Cameleon", widget.Sep.__bases__, dict(widget.Sep.__dict__))

## TODO: POPUP MENU
def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename="/home/matias/.wallpapers/0.jpg",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("/path/to/lock_cmd")
            }
        ),
        PopupImage(
            filename="/home/matias/.wallpapers/0.jpg",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("/path/to/sleep_cmd")
            }
        ),
        PopupImage(
            filename="/home/matias/.wallpapers/0.jpg",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.shutdown()
            }
        ),
        PopupText(
            text="Lock",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            pos_x=0.4,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)
 #}}}

