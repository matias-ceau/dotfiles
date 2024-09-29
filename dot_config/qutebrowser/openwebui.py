# vim :set foldmethod=marker foldmarker=<===,===> :
# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103
config.load_autoconfig(False)
config.source("keybindings.py")
config.source("colors.py")
c.aliases = {
    "w": "session-save",
    "q": "close",
    "qa": "quit",
    "wq": "quit --save",
    "wqa": "quit --save",
    "zotero": "spawn --userscript qute-zotero",
}
c.auto_save.interval = 15000
c.auto_save.session = False
c.session.default_name = "base_session"
c.backend = "webengine"
changelog_after_upgrade = "never"
c.completion.cmd_history_max_items = -1
c.completion.delay = 0
c.completion.favorite_paths = []
c.completion.height = "50%"
c.completion.min_chars = 1
c.completion.open_categories = [
    "filesystem",
]
c.completion.quick = True
c.completion.scrollbar.padding = 2
c.completion.scrollbar.width = 5
c.completion.show = "always"
c.completion.shrink = False
c.completion.timestamp_format = "%Y-%m-%d %H:%M"
c.completion.use_best_match = False
c.completion.web_history.exclude = []
c.completion.web_history.max_items = -1
c.confirm_quit = ["never"]
c.content.autoplay = False
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
]
c.content.blocking.enabled = True
c.content.blocking.hosts.block_subdomains = True
c.content.blocking.hosts.lists = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
]
c.content.blocking.method = "auto"
c.content.blocking.whitelist = []
c.content.cache.size = 268_435_456
c.content.canvas_reading = True
c.content.cookies.accept = "all"
c.content.cookies.store = True
c.content.default_encoding = "utf-8"  # iso-8859-1"
c.content.desktop_capture = "ask"
c.content.dns_prefetch = True
c.content.fullscreen.overlay_timeout = 3000
c.content.fullscreen.window = False
c.content.geolocation = True
c.content.headers.accept_language = "en-US,en;q=0.9"
c.content.headers.custom = {}
c.content.headers.do_not_track = True
c.content.headers.referer = "same-domain"
c.content.headers.user_agent = "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}"
c.content.hyperlink_auditing = False  ## Enable hyperlink auditing (`<a ping>`).
c.content.images = True  ## Load images automatically in web pages.
c.content.javascript.alert = True  ## Show javascript alerts.
c.content.javascript.can_open_tabs_automatically = (
    False  ## Allow JavaScript to open new tabs without user interaction.
)
c.content.javascript.clipboard = "none"
c.content.javascript.enabled = True  ## Enable JavaScript.
c.content.javascript.legacy_touch_events = "never"
c.content.javascript.log = {
    "unknown": "debug",
    "info": "debug",
    "warning": "debug",
    "error": "debug",
}
c.content.javascript.log_message.excludes = {
    "userscript:_qute_stylesheet": [
        "*Refused to apply inline style because it violates the following Content Security Policy directive: *"
    ]
}
c.content.javascript.log_message.levels = {
    "qute:*": ["error"],
    "userscript:GM-*": [],
    "userscript:*": ["error"],
}
c.content.javascript.modal_dialog = True
c.content.javascript.prompt = True  ## Show javascript prompts.
c.content.local_content_can_access_file_urls = (
    True  ## Allow locally loaded documents to access other local URLs.
)
c.content.local_content_can_access_remote_urls = (
    False  ## Allow locally loaded documents to access remote URLs.
)
c.content.local_storage = True  ## Enable support for HTML 5 local storage and Web SQL.
c.content.media.audio_capture = True  ## Allow websites to record audio.
c.content.media.audio_video_capture = True  ## Allow websites to record audio and video. Type: BoolAsk Valid values: true false ask
c.content.media.video_capture = (
    True  ## Allow websites to record video. ## Type: BoolAsk
)
c.content.mouse_lock = "ask"  ## Allow websites to lock your mouse pointer.
c.content.mute = False
c.content.netrc_file = None  ## Netrc-file for HTTP authentication. If unset, `~/.netrc` is used. ## Type: File
c.content.notifications.enabled = (
    "ask"  ## Allow websites to show notifications. ## Type: BoolAsk
)
c.content.notifications.presenter = "auto"
c.content.notifications.show_origin = True
c.content.pdfjs = True  # False
c.content.persistent_storage = "ask"  ## Allow websites to request persistent storage quota via `navigator.webkitPersistentStorage.requestQuota`.
c.content.plugins = True  ## Enable plugins in Web pages.
c.content.prefers_reduced_motion = False
c.content.print_element_backgrounds = (
    True  ## Draw the background color and images also when the page is printed.
)
c.content.private_browsing = False  ## Open new windows in private browsing mode which does not record visited pages.
c.content.proxy = "system"
c.content.register_protocol_handler = "ask"  ## Allow websites to register protocol handlers via `navigator.registerProtocolHandler`. Type: BoolAsk
c.content.site_specific_quirks.enabled = True  ## Enable quirks (such as faked user agent headers) needed to get specific sites to work properly.
c.content.site_specific_quirks.skip = []
c.content.tls.certificate_errors = "ask"
c.content.unknown_url_scheme_policy = "allow-from-user-interaction"
c.content.user_stylesheets = []
c.content.webgl = True  ## Enable WebGL.
c.content.webrtc_ip_handling_policy = "all-interfaces"
c.content.xss_auditing = False
c.downloads.location.directory = "~/Documents"  ## Directory to save downloads to. If unset, a sensible OS-specific default is used.
c.downloads.location.prompt = True  # Prompt the user for the download location. If set to false,`downloads.location.directory` will be used.
c.downloads.location.remember = True  ## Remember the last used download directory.
c.downloads.location.suggestion = "both"
c.downloads.open_dispatcher = None
c.downloads.position = (
    "top"  ## Where to show the downloaded files. ## Valid values:  - top - bottom
)
c.downloads.prevent_mixed_content = True
c.downloads.remove_finished = 5000  ## Duration (in milliseconds) to wait before removing finished downloads. If set to -1, downloads are never removed.
c.editor.command = [
    "alacritty",
    "--class",
    "Alacritty,floating-term",
    "-T",
    "qutebrowser-editor",
    "-e",
    "nvim",
    "{file}",
    "-c",
    "normal {line}G{column0}l",
]
c.editor.encoding = "utf-8"  ## Encoding to use for the editor.
c.editor.remove_file = True  ## Delete the temporary file upon closing the editor.
c.fileselect.handler = "external"
c.fileselect.folder.command = [
    "alacritty",
    "-e",
    "ranger",
    "--show-only-dirs",
    "--choosedir={}",
]
c.fileselect.multiple_files.command = ["alacritty", "-e", "ranger", "--choosefiles={}"]
c.fileselect.single_file.command = ["alacritty", "-e", "ranger", "--choosefile={}"]
c.fonts.default_family = ["Iosevka Nerd Font"]
c.fonts.completion.category = "bold default_size default_family"
c.fonts.completion.entry = "default_size default_family"
c.fonts.contextmenu = "default_size default_family"
c.fonts.debug_console = "default_size default_family"
c.fonts.default_size = "12pt"
c.fonts.downloads = "default_size default_family"
c.fonts.hints = "bold default_size default_family"
c.fonts.keyhint = "default_size default_family"
c.fonts.messages.error = "default_size default_family"
c.fonts.messages.info = "default_size default_family"
c.fonts.messages.warning = "default_size default_family"
c.fonts.prompts = "default_size sans-serif"
c.fonts.statusbar = "default_size default_family"
c.fonts.tabs.selected = "default_size default_family"
c.fonts.tabs.unselected = "default_size default_family"
c.fonts.tooltip = "default_size default_family"
c.fonts.web.family.cursive = "Iosevka Nerd Font"
c.fonts.web.family.fantasy = "Iosevka Nerd Font"
c.fonts.web.family.fixed = "Iosevka Nerd Font"
c.fonts.web.family.sans_serif = "Iosevka Nerd Font"
c.fonts.web.family.serif = "Iosevka Nerd Font"
c.fonts.web.family.standard = "Iosevka Nerd Font"
c.fonts.web.size.default = 16
c.fonts.web.size.default_fixed = 13
c.fonts.web.size.minimum = 0
c.fonts.web.size.minimum_logical = 6
c.hints.auto_follow = "unique-match"
c.hints.auto_follow_timeout = 0
c.hints.border = "1px solid #d0a215"  ## CSS border value for hints.
c.hints.chars = "asdfghjkl"
c.hints.dictionary = "/usr/share/dict/words"
c.hints.hide_unmatched_rapid_hints = True
c.hints.leave_on_load = False  ## Leave hint mode when starting a new page load.
c.hints.min_chars = 1  ## Minimum number of characters used for hint strings.
c.hints.mode = "letter"
c.hints.next_regexes = [
    "\\bnext\\b",
    "\\bmore\\b",
    "\\bnewer\\b",
    "\\b[>→≫]\\b",
    "\\b(>>|»)\\b",
    "\\bcontinue\\b",
]
c.hints.padding = {"top": 0, "bottom": 0, "left": 3, "right": 3}
c.hints.prev_regexes = [
    "\\bprev(ious)?\\b",
    "\\bback\\b",
    "\\bolder\\b",
    "\\b[<←≪]\\b",
    "\\b(<<|«)\\b",
]
c.hints.radius = 6
c.hints.scatter = True  ## Scatter hint key chains (like Vimium) or not (like dwb). Ignored for number hints.
c.hints.selectors = {
    "all": [
        "a",
        "area",
        "textarea",
        "select",
        'input:not([type="hidden"])',
        "button",
        "frame",
        "iframe",
        "img",
        "link",
        "summary",
        '[contenteditable]:not([contenteditable="false"])',
        "[onclick]",
        "[onmousedown]",
        '[role="link"]',
        '[role="option"]',
        '[role="button"]',
        '[role="tab"]',
        '[role="checkbox"]',
        '[role="switch"]',
        '[role="menuitem"]',
        '[role="menuitemcheckbox"]',
        '[role="menuitemradio"]',
        '[role="treeitem"]',
        "[aria-haspopup]",
        "[ng-click]",
        "[ngClick]",
        "[data-ng-click]",
        "[x-ng-click]",
        '[tabindex]:not([tabindex="-1"])',
    ],
    "links": ["a[href]", "area[href]", "link[href]", '[role="link"][href]'],
    "images": ["img"],
    "media": ["audio", "img", "video"],
    "url": ["[src]", "[href]"],
    "inputs": [
        'input[type="text"]',
        'input[type="date"]',
        'input[type="datetime-local"]',
        'input[type="email"]',
        'input[type="month"]',
        'input[type="number"]',
        'input[type="password"]',
        'input[type="search"]',
        'input[type="tel"]',
        'input[type="time"]',
        'input[type="url"]',
        'input[type="week"]',
        "input:not([type])",
        '[contenteditable]:not([contenteditable="false"])',
        "textarea",
    ],
}
c.hints.uppercase = False  ## Make characters in hint strings uppercase.
c.history_gap_interval = 30
c.input.escape_quits_reporter = True  ## Allow Escape to quit the crash reporter.
c.input.forward_unbound_keys = "auto"
c.input.insert_mode.auto_enter = (
    True  ## Enter insert mode if an editable element is clicked.
)
c.input.insert_mode.auto_leave = (
    True  ## Leave insert mode if a non-editable element is clicked.
)
c.input.insert_mode.auto_load = False  ## Automatically enter insert mode if an editable element is focused after loading the page.
c.input.insert_mode.leave_on_load = True  ## Leave insert mode when starting a new page load. Patterns may be unreliable on this setting, and they may match the url you are navigating to, or the URL you are navigating from.
c.input.insert_mode.plugins = (
    False  ## Switch to insert mode when clicking flash and other plugins.
)
c.input.links_included_in_focus_chain = (
    True  ## Include hyperlinks in the keyboard focus chain when tabbing.
)
c.input.match_counts = True  ## Interpret number prefixes as counts for bindings. This enables for vi- like bindings that can be prefixed with a number to indicate a count.
c.input.media_keys = True  ## Whether the underlying Chromium should handle media keys. On Linux, disabling this also disables Chromium's MPRIS integration.
c.input.mode_override = None  ## Mode to change to when focusing on a tab/URL changes. ## Valid values: normal insert passthrough
c.input.mouse.back_forward_buttons = (
    True  ## Enable back and forward buttons on the mouse.
)
c.input.mouse.rocker_gestures = (
    False  ## Enable Opera-like mouse rocker gestures. This disables the context menu.
)
c.input.partial_timeout = 0
c.input.spatial_navigation = False
c.keyhint.blacklist = (
    []
)  ## Keychains that shouldn't be shown in the keyhint dialog. Globs are supported, so `;*` will blacklist all keychains starting with `;`. Use `*` to disable keyhints.
c.keyhint.delay = (
    300  ## Time (in milliseconds) from pressing a key to seeing the keyhint dialog.
)
c.keyhint.radius = (
    6  ## Rounding radius (in pixels) for the edges of the keyhint dialog.
)
c.logging.level.console = "info"  ## Level for console (stdout/stderr) logs. Ignored if the `--loglevel` or `--debug` CLI flags are used. ## Valid values: vdebug debug info warning error critical
c.logging.level.ram = "debug"  ## Level for in-memory logs. ## Valid values: vdebug debug info warning error critical
c.messages.timeout = 3000  ## Duration (in milliseconds) to show messages in the statusbar for. Set to 0 to never clear messages.
c.new_instance_open_target = "window"  # tab
c.new_instance_open_target_window = "last-focused"
c.prompt.filebrowser = True  ## Show a filebrowser in download prompts.
c.prompt.radius = 8  ## Rounding radius (in pixels) for the edges of prompts.
c.qt.args = []
c.qt.chromium.experimental_web_platform_features = "auto"
c.qt.chromium.low_end_device_mode = "auto"
c.qt.chromium.process_model = "process-per-site-instance"
c.qt.chromium.sandboxing = "enable-all"
c.qt.environ = {}
c.qt.force_platform = None
c.qt.force_platformtheme = None
c.qt.force_software_rendering = "none"
c.qt.highdpi = True
c.qt.workarounds.disable_accelerated_2d_canvas = "auto"
c.qt.workarounds.locale = False
c.qt.workarounds.remove_service_workers = False
c.scrolling.bar = "never"
c.scrolling.smooth = False
c.search.ignore_case = "smart"
c.search.incremental = True  ## Find text on a page incrementally, renewing the search for each typed character.
c.search.wrap = True  ## Wrap around at the top and bottom of the page when advancing through ## text matches using `:search-next` and `:search-prev`.
c.search.wrap_messages = True  ## Display messages when advancing through text matches at the top and bottom of the page, e.g. `Search hit TOP`.
c.session.default_name = "openwebui"  ## Name of the session to save by default. If this is set to null, the session which was last loaded is saved. ## Type: SessionName
c.session.lazy_restore = False  ## Load a restored tab as soon as it takes focus.
c.statusbar.padding = {"top": 0, "bottom": 0, "left": 0, "right": 0}
c.statusbar.position = (
    "bottom"  ## Position of the status bar. ## Valid values:  - top  - bottom
)
c.statusbar.show = "never"
c.statusbar.widgets = [
    "search_match",
]
c.tabs.background = True  ## Open new tabs (middleclick/ctrl+click) in the background.
c.tabs.close_mouse_button = "middle"  ## Mouse button with which to close tabs. ## Valid values: ##   - right: Close tabs on right-click. ##   - middle: Close tabs on middle-click. ##   - none: Don't close tabs using the mouse.
c.tabs.close_mouse_button_on_bar = "new-tab"
c.tabs.favicons.scale = 0.8  ## Scaling factor for favicons in the tab bar. The tab size is unchanged, so big favicons also require extra `tabs.padding`.
c.tabs.favicons.show = "never"  ## Valid values: ##   - always: Always show favicons. ##   - never: Always hide favicons. ##   - pinned: Show favicons only on pinned tabs.
c.tabs.focus_stack_size = (
    10  ## Maximum stack size to remember for tab switches (-1 for no maximum).
)
c.tabs.indicator.padding = {
    "top": 2,
    "bottom": 0,
    "left": 0,
    "right": 4,
}  ## Padding (in pixels) for tab indicators.
c.tabs.indicator.width = (
    3  ## Width (in pixels) of the progress indicator (0 to disable).
)
c.tabs.last_close = "ignore"
c.tabs.max_width = -1
c.tabs.min_width = -1
c.tabs.mode_on_change = "normal"
c.tabs.mousewheel_switching = False  ## Switch between tabs using the mouse wheel.
c.tabs.new_position.related = "next"
c.tabs.new_position.stacking = True
c.tabs.new_position.unrelated = "last"
c.tabs.padding = {
    "top": 0,
    "bottom": 0,
    "left": 5,
    "right": 5,
}  ## Padding (in pixels) around text for tabs.
c.tabs.pinned.frozen = True  ## Force pinned tabs to stay at fixed URL.
c.tabs.pinned.shrink = True  ## Shrink pinned tabs down to their contents.
c.tabs.position = "top"  ## Position of the tab bar. ## Valid values: ##   - top ##   - bottom ##   - left ##   - right
c.tabs.select_on_remove = "next"
c.tabs.show = "never"
c.tabs.show_switching_delay = 800  ## Duration (in milliseconds) to show the tab bar before hiding it when tabs.show is set to 'switching'.
c.tabs.tabs_are_windows = True  ## Open a new window for every tab.
c.tabs.title.alignment = (
    "left"  ## Alignment of the text inside of tabs. Valid values: left right center
)
c.tabs.title.elide = "right"  ## Position of ellipsis in truncated title of tabs. ## Valid values: left right middle none
c.tabs.title.format = "{current_title}"
c.tabs.title.format_pinned = ""
c.tabs.undo_stack_size = (
    -1
)  ## Number of closed tabs (per window) and closed windows to remember for :undo (-1 for no maximum).
c.tabs.width = "15%"  ## Width (in pixels or as percentage of the window) of the tab bar if it's vertical. ## Type: PercOrInt
c.tabs.wrap = True  ## Wrap when changing tabs.
c.url.auto_search = "naive"
c.url.default_page = "http://0.0.0.0:8080"
c.url.incdec_segments = ["path", "query"]
c.url.open_base_url = True
c.url.start_pages = ["http://0.0.0.0:8080"]
c.url.yank_ignored_parameters = [
    "ref",
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "utm_name",
]
c.window.hide_decoration = True  # False
c.window.title_format = "OpenWebUI"
c.window.transparent = True
c.zoom.default = "100%"  ## Default zoom level.
c.zoom.levels = [
    "25%",
    "33%",
    "50%",
    "67%",
    "75%",
    "90%",
    "100%",
    "110%",
    "125%",
    "150%",
    "175%",
    "200%",
    "250%",
    "300%",
    "400%",
    "500%",
]
c.zoom.mouse_divider = (
    512  ## Number of zoom increments to divide the mouse wheel movements to.
)
