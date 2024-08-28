import os

from libqtile.config import DropDown, Group, ScratchPad

home = os.path.expanduser("~")


groups = [
    Group("1", label="\u2680"),
    Group("2", label="\u2681"),
    Group("3", label="\u2682"),
    Group("4", label="\u2683"),
    Group("5", label="\u2684"),
    Group("6", label="\u2685"),
    ScratchPad(
        "dock",
        [
            DropDown(
                "terminal",
                ["alacritty", "-T", "terminal"],
                x=0.01,
                y=0,
                width=0.98,
                height=0.8,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "vimwiki",
                [
                    "alacritty",
                    "--working-directory",
                    f"{home}/notes",
                    "-T",
                    "vimwiki",
                    "-e",
                    "nvim",
                    f"{home}/notes/atlas/index.md",
                ],
                x=0.01,
                y=0,
                width=0.98,
                height=0.8,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "ranger",
                ["alacritty", "-T", "ranger", "-e" "ranger"],
                x=0.01,
                y=0,
                width=0.98,
                height=0.8,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "sysmon",
                ["xterm", "-fs", "10", "-e", "btop"],
                x=0.01,
                y=0,
                width=0.98,
                height=0.8,
                opacity=1,
                on_focus_lost_hide=False,
            ),
        ],
        single=True,
    ),
    ScratchPad(
        "scratch",
        [
            DropDown(
                "chatbot",
                ["alacritty", "-e", "aichat"],
                x=0.2,
                width=0.6,
                y=0.2,
                height=0.6,
            ),
            DropDown(
                "note",
                ["alacritty", "-e", "vim", f"{home}/notes/draft.md"],
                x=0.2,
                width=0.6,
                y=0.2,
                height=0.6,
            ),
            DropDown(
                "keepassxc",
                ["keepassxc"],
                x=0.1,
                width=0.8,
                y=0.1,
                height=0.8,
            ),
        ],
    ),
]
