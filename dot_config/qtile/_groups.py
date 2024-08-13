from libqtile.config import Group, ScratchPad, DropDown
import os

home = os.path.expanduser("~")


groups = [
    Group("a", label="\u1d00"),
    Group("z", label="\u1d22"),
    Group("e", label="\u1d07"),
    Group("r", label="\u0280"),
    Group("t", label="\u1d1b"),
    Group("y", label="\u028f"),
    ScratchPad(
        "dock",
        [
            DropDown(
                "terminal",
                ["alacritty"],
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
                ["alacritty", "-e" "ranger"],
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
