from libqtile import layout

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),  # BASIC
    layout.TreeTab(),  # TODO : add auto add_section/sort_sections | section_up/down
    layout.Max(),  # simple full screen
    layout.Matrix(),  # equally spaced +
    layout.MonadTall(),  # 1 big, other small / flip RL / shuffle up down
    layout.MonadThreeCol(),  # same but 3 col (good for widescreen)
    # {{{
    #   layout.Zoomy(),  #
    #   layout.Stack(num_stacks=2),                                                # like columns but only 2 stacks (toggle with W-S-Ret)
    #    layout.Bsp(),                                                              # default same direction auto, change d manually
    #    layout.MonadWide(),                                                        # up down
    #    layout.RatioTile(),                                                        # can be useful instead of matrix
    #    layout.Tile(),                                                             #
    #    layout.VerticalTile(),                                                     #
    # }}}
]

# ScreenSplit() to think about for big monitor
