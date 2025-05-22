import os

# import csv
import socket
import subprocess

from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.popup.toolkit import PopupImage, PopupRelativeLayout, PopupText

hostname = socket.gethostname()
home = os.path.expanduser("~")
scripts = os.environ.get("SCRIPTS")
script_dict = {"xonsh": ".xsh", "sh": ".sh", "python3": ".py"}

# HOST SPECIFIC
scale = 1.0
if hostname == "karhu":
    scale = 0.5

# ----- CMD DICTS / SPECIAL -----(to be modified)----------------------------------------

# QUICKLAUNCHES
notebooks = (
    subprocess.run(["fd", "-tf", r"\.ipynb", home], capture_output=True)
    .stdout.decode()
    .splitlines()
)
nb_commands = [f"jupyter-notebook --browser=chromium {n}" for n in notebooks]
NOTEBOOKS = {k: v for k, v in zip(notebooks, nb_commands)}

## Cameleon widget
if hostname in ["karhu", "korvapuusti", "kirjolohi"]:
    Cameleon = type("Cameleon", widget.Battery.__bases__, dict(widget.Battery.__dict__))
    custom_args = dict(format="{char} {percent:2.0%} {watt:.0f}\u1d21")

    system_clock_args = dict(format="%H%M")

elif (hostname == "karjala") or (hostname == "kukko"):
    Cameleon = type(
        "Cameleon", widget.NvidiaSensors.__bases__, dict(widget.NvidiaSensors.__dict__)
    )
    custom_args = dict(
        format="GPU {temp}°C",
        width=60,
        dpi=96,
    )

    system_clock_args = dict(format="%Y-%m-%d %a %H:%M")

else:
    Cameleon = type("Cameleon", widget.Sep.__bases__, dict(widget.Sep.__dict__))


# }}}
