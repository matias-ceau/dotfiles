# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103
# --------------------------------------------
#                    COLORS
# --------------------------------------------
red = "#d14d41"
red_2 = "#af3029"
orange = "#da702c"
orange_2 = "#bc5215"  #     Warning text     Functions
css_or = "#fceeb8"
yellow = "#d0a215"
yellow_2 = "#ad8301"  #                     Constants
css_ye = "#4d3a0b"
green = "#879a39"
green_2 = "#66800b"  #    Success text     Keywords
css_gr = "#ebf2e7"
cyan = "#3aa99f"
cyan_2 = "#24837b"  #    Links, active    Strings
css_bl = "#142625"
blue = "#4385be"
blue_2 = "#205ea6"  #                    Variables, attributes
purple = "#8b7ec8"
purple_2 = "#5e409d"  #                    Numbers
magenta = "#ce5d97"
magenta_2 = "#a02f6f"  #                    Language featureds
bg = "#100f0f"  #      Background 1
bg_2 = "#1c1b1a"  #    Background 2
ui = "#282726"  #      Borders
ui_2 = "#343331"  #    Hoveredd borders
ui_3 = "#403e3c"  #    Active borders
tx_3 = "#575653"  #    Faint text      Comments
lg_tx_2 = "#6f6e69"
tx_2 = "#878580"  #    Muted text      Punctuation, operators
lg_tx_3 = "#979592"
tx = "#b7b5ac"  #      Primary text
lg_ui_2 = "#cecdc3"
lg_ui = "#dad8ce"
lg_bg_2 = "#e6e4d9"
lg_bg = "#fffcf0"

## Background color of the completion widget category headers. ## Type: QssColor
c.colors.completion.category.bg = (
    f"qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {tx_2}, stop:1 {tx_3})"
)

## Bottom border color of the completion widget category headers. ## Type: QssColor
c.colors.completion.category.border.bottom = bg

## Top border color of the completion widget category headers. ## Type: QssColor
c.colors.completion.category.border.top = bg

## Foreground color of completion widget category headers. ## Type: QtColor
c.colors.completion.category.fg = lg_bg

## Background color of the completion widget for even rows. ## Type: QssColor
c.colors.completion.even.bg = ui_2

## Text color of the completion widget. Either one or list of 3 ## Type: List of QtColor, or QtColor
c.colors.completion.fg = [lg_bg, lg_bg, lg_bg]

## Background color of the selected completion item. ## Type: QssColor
c.colors.completion.item.selected.bg = yellow

## Bottom border color of the selected completion item. ## Type: QssColor
c.colors.completion.item.selected.border.bottom = yellow_2

## Top border color of the selected completion item. ## Type: QssColor
c.colors.completion.item.selected.border.top = yellow_2

## Foreground color of the selected completion item. ## Type: QtColor
c.colors.completion.item.selected.fg = bg

## Foreground color of the matched text in the selected completion item. ## Type: QtColor
c.colors.completion.item.selected.match.fg = red

## Foreground color of the matched text in the completion. ## Type: QtColor
c.colors.completion.match.fg = red

## Background color of the completion widget for odd rows. ## Type: QssColor
c.colors.completion.odd.bg = ui_3

## Color of the scrollbar in the completion view. ## Type: QssColor
c.colors.completion.scrollbar.bg = ui_2

## Color of the scrollbar handle in the completion view. ## Type: QssColor
c.colors.completion.scrollbar.fg = lg_bg

## Background color of disabled items in the context menu. null = Qt default ## Type: QssColor
c.colors.contextmenu.disabled.bg = None

## Foreground color of disabled items in the context menu. If set to null = Qt default ## Type: QssColor
c.colors.contextmenu.disabled.fg = None

## Background color of the context menu. null = Qt default ## Type: QssColor
c.colors.contextmenu.menu.bg = None

## Foreground color of the context menu. null = Qt default ## Type: QssColor
c.colors.contextmenu.menu.fg = None

## Background color of the context menu's selected item. null = Qt default ## Type: QssColor
c.colors.contextmenu.selected.bg = None

## Foreground color of the context menu's selected item. null = Qt default ## Type: QssColor
c.colors.contextmenu.selected.fg = None

## Background color for the download bar. ## Type: QssColor
c.colors.downloads.bar.bg = bg

## Background color for downloads with errors. ## Type: QtColor
c.colors.downloads.error.bg = red

## Foreground color for downloads with errors. ## Type: QtColor
c.colors.downloads.error.fg = lg_bg

## Color gradient start for download backgrounds. ## Type: QtColor
c.colors.downloads.start.bg = blue_2

## Color gradient start for download text. ## Type: QtColor
c.colors.downloads.start.fg = lg_bg

## Color gradient stop for download backgrounds. ## Type: QtColor
c.colors.downloads.stop.bg = green_2

## Color gradient end for download text. ## Type: QtColor
c.colors.downloads.stop.fg = lg_bg

## Color gradient interpolation system for download backgrounds. ## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = "rgb"

## Color gradient interpolation system for download text.
## Type: ColorSystem ##   - rgb ##   - hsv ##   - hsl ##   - none
c.colors.downloads.system.fg = "rgb"

## Background color for hints. Note that you can use a `rgba(...)` value for transparency. ## Type: QssColor
c.colors.hints.bg = "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(252, 238, 184, 0.8), stop:1 rgba(208, 162, 21, 0.8))"

## Font color for hints. ## Type: QssColor
c.colors.hints.fg = bg

## Font color for the matched part of hints. ## Type: QtColor
c.colors.hints.match.fg = "green"

## Background color of the keyhint widget. ## Type: QssColor
c.colors.keyhint.bg = "rgba(0, 0, 0, 80%)"

## Text color for the keyhint widget. ## Type: QssColor
c.colors.keyhint.fg = lg_bg

## Highlight color for keys to complete the current keychain. ## Type: QssColor
c.colors.keyhint.suffix.fg = yellow

## Background color of an error message. ## Type: QssColor
c.colors.messages.error.bg = red

## Border color of an error message. ## Type: QssColor
c.colors.messages.error.border = red_2

## Foreground color of an error message. ## Type: QssColor
c.colors.messages.error.fg = lg_bg

## Background color of an info message. ## Type: QssColor
c.colors.messages.info.bg = bg

## Border color of an info message. ## Type: QssColor
c.colors.messages.info.border = ui_2

## Foreground color of an info message. ## Type: QssColor
c.colors.messages.info.fg = lg_bg

## Background color of a warning message. ## Type: QssColor
c.colors.messages.warning.bg = orange_2

## Border color of a warning message. ## Type: QssColor
c.colors.messages.warning.border = orange

## Foreground color of a warning message. ## Type: QssColor
c.colors.messages.warning.fg = bg

## Background color for prompts. ## Type: QssColor
c.colors.prompts.bg = ui_3

## Border used around UI elements in prompts. ## Type: String
c.colors.prompts.border = "1px solid gray"

## Foreground color for prompts. ## Type: QssColor
c.colors.prompts.fg = lg_bg

## Background color for the selected item in filename prompts. ## Type: QssColor
c.colors.prompts.selected.bg = ui

## Foreground color for the selected item in filename prompts. ## Type: QssColor
c.colors.prompts.selected.fg = lg_bg

## Background color of the statusbar in caret mode. ## Type: QssColor
c.colors.statusbar.caret.bg = purple_2

## Foreground color of the statusbar in caret mode. ## Type: QssColor
c.colors.statusbar.caret.fg = lg_bg

## Background color of the statusbar in caret mode with a selection. ## Type: QssColor
c.colors.statusbar.caret.selection.bg = magenta

## Foreground color of the statusbar in caret mode with a selection. ## Type: QssColor
c.colors.statusbar.caret.selection.fg = lg_bg

## Background color of the statusbar in command mode. ## Type: QssColor
c.colors.statusbar.command.bg = bg

## Foreground color of the statusbar in command mode. ## Type: QssColor
c.colors.statusbar.command.fg = lg_bg

## Background color of the statusbar in private browsing + command mode. ## Type: QssColor
c.colors.statusbar.command.private.bg = "darkslategray"

## Foreground color of the statusbar in private browsing + command mode. ## Type: QssColor
c.colors.statusbar.command.private.fg = lg_bg

## Background color of the statusbar in insert mode. ## Type: QssColor
c.colors.statusbar.insert.bg = green_2

## Foreground color of the statusbar in insert mode. ## Type: QssColor
c.colors.statusbar.insert.fg = lg_bg

## Background color of the statusbar. ## Type: QssColor
c.colors.statusbar.normal.bg = bg

## Foreground color of the statusbar. ## Type: QssColor
c.colors.statusbar.normal.fg = lg_bg

## Background color of the statusbar in passthrough mode. ## Type: QssColor
c.colors.statusbar.passthrough.bg = blue_2

## Foreground color of the statusbar in passthrough mode. ## Type: QssColor
c.colors.statusbar.passthrough.fg = lg_bg

## Background color of the statusbar in private browsing mode. ## Type: QssColor
c.colors.statusbar.private.bg = lg_tx_2

## Foreground color of the statusbar in private browsing mode. ## Type: QssColor
c.colors.statusbar.private.fg = lg_bg

## Background color of the progress bar. ## Type: QssColor
c.colors.statusbar.progress.bg = lg_bg

## Foreground color of the URL in the statusbar on error. ## Type: QssColor
c.colors.statusbar.url.error.fg = orange

## Default foreground color of the URL in the statusbar. ## Type: QssColor
c.colors.statusbar.url.fg = lg_bg

## Foreground color of the URL in the statusbar for hovered links. ## Type: QssColor
c.colors.statusbar.url.hover.fg = cyan

## Foreground color of the URL in the statusbar on successful load ## (http). ## Type: QssColor
c.colors.statusbar.url.success.http.fg = lg_bg

## Foreground color of the URL in the statusbar on successful load ## (https). ## Type: QssColor
c.colors.statusbar.url.success.https.fg = green

## Foreground color of the URL in the statusbar when there's a warning. ## Type: QssColor
c.colors.statusbar.url.warn.fg = yellow

## Background color of the tab bar. ## Type: QssColor
c.colors.tabs.bar.bg = tx_3

## Background color of unselected even tabs. ## Type: QtColor
c.colors.tabs.even.bg = "darkgrey"

## Foreground color of unselected even tabs. ## Type: QtColor
c.colors.tabs.even.fg = lg_bg

## Color for the tab indicator on errors. ## Type: QtColor
c.colors.tabs.indicator.error = red_2

## Color gradient start for the tab indicator. ## Type: QtColor
c.colors.tabs.indicator.start = blue_2

## Color gradient end for the tab indicator. ## Type: QtColor
c.colors.tabs.indicator.stop = green

## Color gradient interpolation system for the tab indicator. ## Type: ColorSystem
c.colors.tabs.indicator.system = "rgb"

## Background color of unselected odd tabs. ## Type: QtColor
c.colors.tabs.odd.bg = ui

## Foreground color of unselected odd tabs. ## Type: QtColor
c.colors.tabs.odd.fg = lg_bg

## Background color of pinned unselected even tabs. ## Type: QtColor
c.colors.tabs.pinned.even.bg = cyan_2

## Foreground color of pinned unselected even tabs. ## Type: QtColor
c.colors.tabs.pinned.even.fg = lg_bg

## Background color of pinned unselected odd tabs. ## Type: QtColor
c.colors.tabs.pinned.odd.bg = cyan

## Foreground color of pinned unselected odd tabs. ## Type: QtColor
c.colors.tabs.pinned.odd.fg = lg_bg

## Background color of pinned selected even tabs. ## Type: QtColor
c.colors.tabs.pinned.selected.even.bg = bg

## Foreground color of pinned selected even tabs. ## Type: QtColor
c.colors.tabs.pinned.selected.even.fg = lg_bg

## Background color of pinned selected odd tabs. ## Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = bg

## Foreground color of pinned selected odd tabs. ## Type: QtColor
c.colors.tabs.pinned.selected.odd.fg = lg_bg

## Background color of selected even tabs. ## Type: QtColor
c.colors.tabs.selected.even.bg = bg

## Foreground color of selected even tabs. ## Type: QtColor
c.colors.tabs.selected.even.fg = lg_bg

## Background color of selected odd tabs. ## Type: QtColor
c.colors.tabs.selected.odd.bg = bg

## Foreground color of selected odd tabs. ## Type: QtColor
c.colors.tabs.selected.odd.fg = lg_bg

## Background color of tooltips. If set to null, the Qt default is used. ## Type: QssColor
c.colors.tooltip.bg = None

## Foreground color of tooltips. If set to null, the Qt default is used. ## Type: QssColor
c.colors.tooltip.fg = None

## Background color for webpages if unset (or empty to use the theme's color). ## Type: QtColor
c.colors.webpage.bg = None

## Which algorithm to use for modifying how colors are rendered with dark mode. The `lightness-cielab` value was added with QtWebEngine 5.14 and is treated like `lightness-hsl` with older QtWebEngine versions. ## Type: String
## Valid values:
##   - lightness-cielab: Modify colors by converting them to CIELAB color space and inverting the L value. Not available with Qt < 5.14.
##   - lightness-hsl: Modify colors by converting them to the HSL color space and inverting the lightness (i.e. the "L" in HSL).
##   - brightness-rgb: Modify colors by subtracting each of r, g, and b from their maximum value.
c.colors.webpage.darkmode.algorithm = "lightness-cielab"

## Contrast for dark mode. This only has an effect when `colors.webpage.darkmode.algorithm` is set to `lightness-hsl` or `brightness-rgb`. ## Type: Float
c.colors.webpage.darkmode.contrast: float = 0.0

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
