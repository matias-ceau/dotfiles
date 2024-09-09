# from __future__ import annotations
# from libqtile.log_utils import logger
import re

# _custom : custom widgets/scripts/pop ups
# _style : colors, decorations
from _groups import groups
from _hooks import *
from _keys import keys, mouse
from _layouts import layouts
from _screens import screens
from libqtile import layout
from libqtile.config import Match

terminal = "kitty"  # guess_terminal()

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="qjackctl"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="pinentry-gtk-2"),  # GPG key password entry
        Match(title="fzfmenu"),
        Match(title="floating"),
        Match(title="wallpaper_select"),
        Match(wm_class="keepassxc"),
        Match(wm_class=re.compile(r".*floating.*")),
        Match(title=re.compile(r".*floating.*")),
    ]
)

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = False  # True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False  # True
wl_input_rules = None
wmname = "LG3D"
