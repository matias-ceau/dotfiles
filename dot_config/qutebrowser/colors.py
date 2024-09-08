# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103
# --------------------------------------------
#                    COLORS
# --------------------------------------------
f_red = "#d14d41"
f_red_2 = "#af3029"
f_orange = "#da702c"
f_orange_2 = "#bc5215"  #     Warning text     Functions
css_or = "#fceeb8"
f_yellow = "#d0a215"
f_yellow_2 = "#ad8301"  #                     Constants
css_ye = "#4d3a0b"
f_green = "#879a39"
f_green_2 = "#66800b"  #    Success text     Keywords
css_gr = "#ebf2e7"
f_cyan = "#3aa99f"
f_cyan_2 = "#24837b"  #    Links, active    Strings
css_bl = "#142625"
f_blue = "#4385be"
f_blue_2 = "#205ea6"  #                    Variables, attributes
f_purple = "#8b7ec8"
f_purple_2 = "#5e409d"  #                    Numbers
f_magenta = "#ce5d97"
f_magenta_2 = "#a02f6f"  #                    Language featureds
f_black = "#100f0f"  #      Background 1
base950 = "#1c1b1a"  #    Background 2
base900 = "#282726"  #      Borders
base850 = "#343331"  #    Hoveredd borders
base800 = "#403e3c"  #    Active borders
base700 = "#575653"  #    Faint text      Comments
base600 = "#6f6e69"
base500 = "#878580"  #    Muted text      Punctuation, operators
base300 = "#979592"
base200 = "#b7b5ac"  #      Primary text
base150 = "#cecdc3"
base100 = "#dad8ce"
base50 = "#e6e4d9"
f_white = "#fffcf0"

## Background color of the completion widget category headers. ## Type: QssColor
c.colors.completion.category.bg = "#000000"  # ( f"qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {tx_2}, stop:1 {tx_3})")
## Foreground color of completion widget category headers. ## Type: QtColor
c.colors.completion.category.fg = f_magenta
## Bottom and top border color of the completion widget category headers. ## Type: QssColor
c.colors.completion.category.border.top = base950
c.colors.completion.category.border.bottom = base950

## Text color of the completion widget. Either one or list of 3 ## Type: List of QtColor, or QtColor
c.colors.completion.fg = [f_white, f_white, f_white]
## Background color of the completion widget for even rows. ## Type: QssColor
c.colors.completion.odd.bg = f_black
c.colors.completion.even.bg = base950

## Bottom and top border color of the selected completion item. ## Type: QssColor
c.colors.completion.item.selected.fg = f_black
c.colors.completion.item.selected.bg = f_yellow_2
c.colors.completion.item.selected.border.top = f_yellow_2
c.colors.completion.item.selected.border.bottom = f_yellow_2

## Foreground color of the matched text in the selected completion item. ## Type: QtColor
c.colors.completion.item.selected.match.fg = f_white

## Foreground color of the matched text in the completion. ## Type: QtColor
c.colors.completion.match.fg = f_yellow

## Color of the scrollbar in the completion view. ## Type: QssColor
c.colors.completion.scrollbar.fg = base900
c.colors.completion.scrollbar.bg = base850

## Background color of disabled items in the context menu. null = Qt default ## Type: QssColor
c.colors.contextmenu.disabled.fg = None
c.colors.contextmenu.disabled.bg = None

## Background color of the context menu. null = Qt default ## Type: QssColor
c.colors.contextmenu.menu.fg = None
c.colors.contextmenu.menu.bg = None

## Background color of the context menu's selected item. null = Qt default ## Type: QssColor
c.colors.contextmenu.selected.fg = None
c.colors.contextmenu.selected.bg = None

## Background color for the download bar. ## Type: QssColor
c.colors.downloads.bar.bg = f_black

## Background color for downloads with errors. ## Type: QtColor
c.colors.downloads.error.fg = f_white
c.colors.downloads.error.bg = f_red

## Color gradient start for download backgrounds. ## Type: QtColor
c.colors.downloads.start.fg = f_white
c.colors.downloads.start.bg = f_blue_2

## Color gradient stop for download backgrounds. ## Type: QtColor
c.colors.downloads.stop.fg = f_white
c.colors.downloads.stop.bg = f_green_2

## Color gradient interpolation system for download backgrounds. ## Type: ColorSystem
## Valid values: rgb hsv hsl none
c.colors.downloads.system.bg = "rgb"

## Color gradient interpolation system for download text.
## Type: ColorSystem  rgb - hsv - hsl  none
c.colors.downloads.system.fg = "rgb"

## Background color for hints. Note that you can use a `rgba(...)` value for transparency. ## Type: QssColor
c.colors.hints.fg = f_black
c.colors.hints.bg = "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(252, 238, 184, 0.8), stop:1 rgba(208, 162, 21, 0.8))"

## Font color for the matched part of hints. ## Type: QtColor
c.colors.hints.match.fg = f_red

## Background color of the keyhint widget. ## Type: QssColor
c.colors.keyhint.fg = f_white
c.colors.keyhint.bg = "rgba(0, 0, 0, 90%)"
## Highlight color for keys to complete the current keychain. ## Type: QssColor
c.colors.keyhint.suffix.fg = f_yellow

## Background color of an error message. ## Type: QssColor
c.colors.messages.error.fg = f_white
c.colors.messages.error.bg = f_red
c.colors.messages.error.border = f_red_2

## Background color of an info message. ## Type: QssColor
c.colors.messages.info.fg = f_white
c.colors.messages.info.bg = f_black
c.colors.messages.info.border = base850

## Background color of a warning message. ## Type: QssColor
c.colors.messages.warning.fg = f_black
c.colors.messages.warning.bg = f_orange_2
c.colors.messages.warning.border = f_orange

## Background color for prompts. ## Type: QssColor
c.colors.prompts.bg = base800
c.colors.prompts.fg = f_white
c.colors.prompts.border = "1px solid gray"

## Background color for the selected item in filename prompts. ## Type: QssColor
c.colors.prompts.selected.bg = base900
c.colors.prompts.selected.fg = f_white

## Background color of the statusbar in caret mode. ## Type: QssColor
c.colors.statusbar.caret.fg = f_green
c.colors.statusbar.caret.bg = f_black

## Background color of the statusbar in caret mode with a selection. ## Type: QssColor
c.colors.statusbar.caret.selection.fg = f_green
c.colors.statusbar.caret.selection.bg = f_black

## Background color of the statusbar in command mode. ## Type: QssColor
c.colors.statusbar.command.fg = f_blue
c.colors.statusbar.command.bg = f_black

## Background color of the statusbar in insert mode. ## Type: QssColor
c.colors.statusbar.insert.fg = f_cyan
c.colors.statusbar.insert.bg = base850

## Background color of the statusbar. ## Type: QssColor
c.colors.statusbar.normal.fg = f_yellow
c.colors.statusbar.normal.bg = f_black

## Background color of the statusbar in passthrough mode. ## Type: QssColor
c.colors.statusbar.passthrough.fg = f_purple
c.colors.statusbar.passthrough.bg = f_black

## Background color of the statusbar in private browsing mode. ## Type: QssColor
c.colors.statusbar.private.fg = base700
c.colors.statusbar.private.bg = f_purple_2

## Background color of the statusbar in private browsing + command mode. ## Type: QssColor
c.colors.statusbar.command.private.fg = base800
c.colors.statusbar.command.private.bg = f_purple

## Background color of the progress bar. ## Type: QssColor
c.colors.statusbar.progress.bg = f_white

## Foreground color of the URL in the statusbar on error. ## Type: QssColor
c.colors.statusbar.url.fg = f_white
c.colors.statusbar.url.error.fg = f_orange
c.colors.statusbar.url.warn.fg = f_yellow
## Foreground color of the URL in the statusbar for hovered links. ## Type: QssColor
c.colors.statusbar.url.hover.fg = f_cyan
## Foreground color of the URL in the statusbar on successful load ## (https). ## Type: QssColor
c.colors.statusbar.url.success.https.fg = f_green

## Background color of the tab bar. ## Type: QssColor
c.colors.tabs.bar.bg = f_black

## Background color of unselected even tabs. ## Type: QtColor
c.colors.tabs.odd.fg = f_white
c.colors.tabs.even.fg = f_white
c.colors.tabs.odd.bg = base900
c.colors.tabs.even.bg = base900

## Background color of selected even tabs. ## Type: QtColor
c.colors.tabs.selected.even.fg = f_yellow
c.colors.tabs.selected.odd.fg = f_yellow
c.colors.tabs.selected.even.bg = "#000000"
c.colors.tabs.selected.odd.bg = "#000000"

## Color for the tab indicator on errors. ## Type: QtColor
c.colors.tabs.indicator.error = f_red_2

## Color gradient start for the tab indicator. ## Type: QtColor
c.colors.tabs.indicator.start = f_magenta
## Color gradient end for the tab indicator. ## Type: QtColor
c.colors.tabs.indicator.stop = f_magenta_2

## Color gradient interpolation system for the tab indicator. ## Type: ColorSystem
c.colors.tabs.indicator.system = "rgb"

## Background color of pinned unselected even tabs. ## Type: QtColor
c.colors.tabs.pinned.even.fg = f_white
c.colors.tabs.pinned.odd.fg = f_white
c.colors.tabs.pinned.selected.even.fg = f_yellow
c.colors.tabs.pinned.selected.odd.fg = f_yellow
# background
c.colors.tabs.pinned.odd.bg = f_magenta_2
c.colors.tabs.pinned.even.bg = f_magenta_2
c.colors.tabs.pinned.selected.odd.bg = f_black
c.colors.tabs.pinned.selected.even.bg = f_black


## Background color of tooltips. If set to null, the Qt default is used. ## Type: QssColor
c.colors.tooltip.fg = None
c.colors.tooltip.bg = None

## Background color for webpages if unset (or empty to use the theme's color). ## Type: QtColor
c.colors.webpage.bg = None

## Which algorithm to use for modifying how colors are rendered with dark mode. The `lightness-cielab` value was added with QtWebEngine 5.14 and is treated like `lightness-hsl` with older QtWebEngine versions. ## Type: String
## Valid values:
##   - lightness-cielab: Modify colors by converting them to CIELAB color space and inverting the L value. Not available with Qt < 5.14.
##   - lightness-hsl: Modify colors by converting them to the HSL color space and inverting the lightness (i.e. the "L" in HSL).
##   - brightness-rgb: Modify colors by subtracting each of r, g, and b from their maximum value.
c.colors.webpage.darkmode.algorithm = "lightness-cielab"

## Contrast for dark mode. This only has an effect when `colors.webpage.darkmode.algorithm` is set to `lightness-hsl` or `brightness-rgb`. ## Type: Float
c.colors.webpage.darkmode.contrast = 0.0

## Render all web contents using a dark theme. On QtWebEngine < 6.7, this setting requires a restart and does not support URL patterns, only the global setting is applied. Example configurations from Chromium's
## `chrome://flags`: - "With simple HSL/CIELAB/RGB-based inversion": Set
## `colors.webpage.darkmode.algorithm` accordingly, and   set
## `colors.webpage.darkmode.policy.images` to `never`.  - "With selective
## image inversion": qutebrowser default settings.
## Type: Bool
c.colors.webpage.darkmode.enabled = False
# True

## Which images to apply dark mode to.
## Type: String
## Valid values:
##   - always: Apply dark mode filter to all images.
##   - never: Never apply dark mode filter to any images.
##   - smart: Apply dark mode based on image content. Not available with Qt 5.15.0.
##   - smart-simple: On QtWebEngine 6.6, use a simpler algorithm for smart mode (based on numbers of colors and transparency), rather than an ML-based model. Same as 'smart' on older QtWebEnigne versions.
c.colors.webpage.darkmode.policy.images = "smart"

## Which pages to apply dark mode to. The underlying Chromium setting has
## been removed in QtWebEngine 5.15.3, thus this setting is ignored
## there. Instead, every element is now classified individually.
## Type: String
## Valid values:
##   - always: Apply dark mode filter to all frames, regardless of content.
##   - smart: Apply dark mode filter to frames based on background color.
c.colors.webpage.darkmode.policy.page = "smart"

## Threshold for inverting background elements with dark mode. Background
## elements with brightness above this threshold will be inverted, and
## below it will be left as in the original, non-dark-mode page. Set to
## 256 to never invert the color or to 0 to always invert it. Note: This
## behavior is the opposite of
## `colors.webpage.darkmode.threshold.foreground`!
## Type: Int
c.colors.webpage.darkmode.threshold.background = 0

## Threshold for inverting text with dark mode. Text colors with
## brightness below this threshold will be inverted, and above it will be
## left as in the original, non-dark-mode page. Set to 256 to always
## invert text color or to 0 to never invert text color.
## Type: Int
c.colors.webpage.darkmode.threshold.foreground = 256

## Value to use for `prefers-color-scheme:` for websites. The "light"
## value is only available with QtWebEngine 5.15.2+. On older versions,
## it is the same as "auto". The "auto" value is broken on QtWebEngine
## 5.15.2 due to a Qt bug. There, it will fall back to "light"
## unconditionally.
## Type: String
## Valid values:
##   - auto: Use the system-wide color scheme setting.
##   - light: Force a light theme.
##   - dark: Force a dark theme.
c.colors.webpage.preferred_color_scheme = "dark"
#
