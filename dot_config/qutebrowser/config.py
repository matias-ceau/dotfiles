# vim :set foldmethod=marker ; foldmarker=<===,===> :
# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103

# <===  Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html
## AUTOCONFIG.YAML
## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.#
# ===>
config.load_autoconfig(False)
config.source("keybindings.py")
config.source("colors.py")

# --------------------------------------------
#   ALIASES
# --------------------------------------------

# <===  Aliases for commands. The keys of the given dictionary are the
## aliases, while the values are the commands they map to.
## Type: Dict
# ===>
c.aliases = {
    "w": "session-save",
    "q": "close",
    "wq": "quit --save",
    "dark": "set colors.webpage.darkmode.enabled",
    "zotero": "spawn --userscript qute-zotero",
}

# <===  Time interval (in milliseconds) between auto-saves of
## config/cookies/etc.
## Type: Int
# ===>
c.auto_save.interval = 15000

# <===  Always restore open sites when qutebrowser is reopened. Without this
## option set, `:wq` (`:quit --save`) needs to be used to save open tabs
## (and restore them), while quitting qutebrowser in any other way will
## not save/restore the session. By default, this will save to the
## session which was last loaded. This behavior can be customized via the
## `session.default_name` setting.
## Type: Bool
# ===>
c.auto_save.session = False
c.session.default_name = "default"

# <===  Backend to use to display websites. qutebrowser supports two different
## web rendering engines / backends, QtWebEngine and QtWebKit (not
## recommended). QtWebEngine is Qt's official successor to QtWebKit, and
## both the default/recommended backend. It's based on a stripped-down
## Chromium and regularly updated with security fixes and new features by
## the Qt project: https://wiki.qt.io/QtWebEngine QtWebKit was
## qutebrowser's original backend when the project was started. However,
## support for QtWebKit was discontinued by the Qt project with Qt 5.6 in
## 2016. The development of QtWebKit was picked up in an official fork:
## https://github.com/qtwebkit/qtwebkit - however, the project seems to
## have stalled again. The latest release (5.212.0 Alpha 4) from March
## 2020 is based on a WebKit version from 2016, with many known security
## vulnerabilities. Additionally, there is no process isolation and
## sandboxing. Due to all those issues, while support for QtWebKit is
## still available in qutebrowser for now, using it is strongly
## discouraged.
## Type: String
## Valid values:
##   - webengine: Use QtWebEngine (based on Chromium - recommended).
##   - webkit: Use QtWebKit (based on WebKit, similar to Safari - many known security issues!).
# ===>
c.backend = "webengine"

# <===  When to show a changelog after qutebrowser was upgraded.
## Type: String
## Valid values:
##   - major: Show changelog for major upgrades (e.g. v2.0.0 -> v3.0.0).
##   - minor: Show changelog for major and minor upgrades (e.g. v2.0.0 -> v2.1.0).
##   - patch: Show changelog for major, minor and patch upgrades (e.g. v2.0.0 -> v2.0.1).
##   - never: Never show changelog after upgrades.
# ===>
changelog_after_upgrade = "patch"

# --------------------------------------------
#                    COMPLETIONS
# --------------------------------------------
# <===  Number of commands to save in the command history. 0: no history / -1:
## unlimited
## Type: Int
# ===>
c.completion.cmd_history_max_items = -1

# <===  Delay (in milliseconds) before updating completions after typing a
## character.
## Type: Int
# ===>
c.completion.delay = 0

# <===  Default filesystem autocomplete suggestions for :open. The elements of
## this list show up in the completion window under the Filesystem
## category when the command line contains `:open` but no argument.
## Type: List of String TODO:
# ===>
c.completion.favorite_paths = []

# <===  Height (in pixels or as percentage of the window) of the completion.
## Type: PercOrInt
# ===>
c.completion.height = "50%"

# <===  Minimum amount of characters needed to update completions.
## Type: Int
# ===>
c.completion.min_chars = 1

# <===  Which categories to show (in which order) in the :open completion.
## Type: FlagList
## Valid values: - searchengines - quickmarks - bookmarks - history - filesystem
# ===>
c.completion.open_categories = [
    "quickmarks",
    "bookmarks",
    "history",
    "filesystem",
    "searchengines",
]

# <===  Move on to the next part when there's only one possible completion
## left.
## Type: Bool
# ===>
c.completion.quick = True

# <===  Padding (in pixels) of the scrollbar handle in the completion window.
## Type: Int
# ===>
c.completion.scrollbar.padding = 2

# <===  Width (in pixels) of the scrollbar in the completion window.
## Type: Int
# ===>
c.completion.scrollbar.width = 5

# <===  When to show the autocompletion window.
## Type: String
## Valid values:
##   - always: Whenever a completion is available.
##   - auto: Whenever a completion is requested.
##   - never: Never.
# ===>
c.completion.show = "always"

# <===  Shrink the completion to be smaller than the configured size if there
## are no scrollbars.
## Type: Bool
# ===>
c.completion.shrink = False

# <===  Format of timestamps (e.g. for the history completion). See
## https://sqlite.org/lang_datefunc.html and
## https://docs.python.org/3/library/datetime.html#strftime-strptime-
## behavior for allowed substitutions, qutebrowser uses both sqlite and
## Python to format its timestamps.
## Type: String
# ===>
c.completion.timestamp_format = "%Y-%m-%d %H:%M"

# <===  Execute the best-matching command on a partial match.
## Type: Bool
# ===>
c.completion.use_best_match = False

# <===  A list of patterns which should not be shown in the history. This only
## affects the completion. Matching URLs are still saved in the history
## (and visible on the `:history` page), but hidden in the completion.
## Changing this setting will cause the completion history to be
## regenerated on the next start, which will take a short while.
## Type: List of UrlPattern
# ===>
c.completion.web_history.exclude = []

# <===  Number of URLs to show in the web history. 0: no history / -1:
## unlimited
## Type: Int
# ===>
c.completion.web_history.max_items = -1

# <===  Require a confirmation before quitting the application.
## Type: ConfirmQuit
## Valid values:
##   - always: Always show a confirmation.
##   - multiple-tabs: Show a confirmation if multiple tabs are opened.
##   - downloads: Show a confirmation if downloads are running
##   - never: Never show a confirmation.
# ===>
c.confirm_quit = ["never"]

# --------------------------------------------
#                    COMPLETIONS
# --------------------------------------------
# <===  Automatically start playing `<video>` elements.
## Type: Bool
# ===>
c.content.autoplay = False

# <===  List of URLs to ABP-style adblocking rulesets.  Only used when Brave's
## ABP-style adblocker is used (see `content.blocking.method`).  You can
## find an overview of available lists here:
## https://adblockplus.org/en/subscriptions - note that the special
## `subscribe.adblockplus.org` links aren't handled by qutebrowser, you
## will instead need to find the link to the raw `.txt` file (e.g. by
## extracting it from the `location` parameter of the subscribe URL and
## URL-decoding it).
## Type: List of Url TODO
# ===>
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
]

# <===  Enable the ad/host blocker
## Type: Bool
# ===>
c.content.blocking.enabled = True

# <===  Block subdomains of blocked hosts. Note: If only a single subdomain is
## blocked but should be allowed, consider using
## `content.blocking.whitelist` instead.
## Type: Bool
# ===>
c.content.blocking.hosts.block_subdomains = True

# <===  List of URLs to host blocklists for the host blocker.  Only used when
## the simple host-blocker is used (see `content.blocking.method`).  The
## file can be in one of the following formats:  - An `/etc/hosts`-like
## file - One host per line - A zip-file of any of the above, with either
## only one file, or a file   named `hosts` (with any extension).  It's
## also possible to add a local file or directory via a `file://` URL. In
## case of a directory, all files in the directory are read as adblock
## lists.  The file `~/.config/qutebrowser/blocked-hosts` is always read
## if it exists.
## Type: List of Url
# ===>
c.content.blocking.hosts.lists = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
]

# <===  Which method of blocking ads should be used.  Support for Adblock Plus
## (ABP) syntax blocklists using Brave's Rust library requires the
## `adblock` Python package to be installed, which is an optional
## dependency of qutebrowser. It is required when either `adblock` or
## `both` are selected.
## Type: String
## Valid values:
##   - auto: Use Brave's ABP-style adblocker if available, host blocking otherwise
##   - adblock: Use Brave's ABP-style adblocker
##   - hosts: Use hosts blocking
##   - both: Use both hosts blocking and Brave's ABP-style adblocker
# ===>
c.content.blocking.method = "both"

# <===  A list of patterns that should always be loaded, despite being blocked
## by the ad-/host-blocker. Local domains are always exempt from
## adblocking. Note this whitelists otherwise blocked requests, not
## first-party URLs. As an example, if `example.org` loads an ad from
## `ads.example.org`, the whitelist entry could be
## `https://ads.example.org/*`. If you want to disable the adblocker on a
## given page, use the `content.blocking.enabled` setting with a URL
## pattern instead.
## Type: List of UrlPattern
# ===>
c.content.blocking.whitelist = []

# <===  Enable support for the HTML 5 web application cache feature. An
## application cache acts like an HTTP cache in some sense. For documents
## that use the application cache via JavaScript, the loader engine will
## first ask the application cache for the contents, before hitting the
## network.
## Type: Bool
# ===>
# c.content.cache.appcache = True #unavailable?

# <===  Maximum number of pages to hold in the global memory page cache. The
## page cache allows for a nicer user experience when navigating forth or
## back to pages in the forward/back history, by pausing and resuming up
## to _n_ pages. For more information about the feature, please refer to:
## https://webkit.org/blog/427/webkit-page-cache-i-the-basics/
## Type: Int
# ===>
# c.content.cache.maximum_pages = 30 #unavailable?

# <===  Size (in bytes) of the HTTP network cache. Null to use the default
## value. With QtWebEngine, the maximum supported value is 2147483647 (~2
## GB).
## Type: Int
# ===>
c.content.cache.size = 268_435_456

# <===  Allow websites to read canvas elements. Note this is needed for some
## websites to work properly. On QtWebEngine < 6.6, this setting requires
## a restart and does not support URL patterns, only the global setting
## is applied.
## Type: Bool
# ===>
c.content.canvas_reading = True

# <===  Which cookies to accept. With QtWebEngine, this setting also controls
## other features with tracking capabilities similar to those of cookies;
## including IndexedDB, DOM storage, filesystem API, service workers, and
## AppCache. Note that with QtWebKit, only `all` and `never` are
## supported as per-domain values. Setting `no-3rdparty` or `no-
## unknown-3rdparty` per-domain on QtWebKit will have the same effect as
## `all`. If this setting is used with URL patterns, the pattern gets
## applied to the origin/first party URL of the page making the request,
## not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
## from URLs, so URL patterns using paths will not match. With
## QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
## you will typically need to set this setting for `example.com` when the
## cookie is set on `somesubdomain.example.com` for it to work properly.
## To debug issues with this setting, start qutebrowser with `--debug
## --logfilter network --debug-flag log-cookies` which will show all
## cookies being set.
## Type: String
## Valid values:
##   - all: Accept all cookies.
##   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
##   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
##   - never: Don't accept cookies at all.
# ===>
c.content.cookies.accept = "all"

# <===  Store cookies.
## Type: Bool
# ===>
c.content.cookies.store = True

# <===  Default encoding to use for websites. The encoding must be a string
## describing an encoding such as _utf-8_, _iso-8859-1_, etc.
## Type: String
# ===>
c.content.default_encoding = "utf-8"  # iso-8859-1"

# <===  Allow websites to share screen content.
## Type: BoolAsk
## Valid values: - true - false - ask
# ===>
c.content.desktop_capture = "ask"

# <===  Try to pre-fetch DNS entries to speed up browsing.
## Type: Bool
# ===>
c.content.dns_prefetch = True

# <===  Expand each subframe to its contents. This will flatten all the frames
## to become one scrollable page.
## Type: Bool
# ===>
# c.content.frame_flattening = False #unavailable?

# <===  Set fullscreen notification overlay timeout in milliseconds. If set to
## 0, no overlay will be displayed.
## Type: Int
# ===>
c.content.fullscreen.overlay_timeout = 3000

# <===  Limit fullscreen to the browser window (does not expand to fill the
## screen).
## Type: Bool
# ===>
c.content.fullscreen.window = False

# <===  Allow websites to request geolocations.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# ===>
c.content.geolocation = "ask"

# <===  Value to send in the `Accept-Language` header. Note that the value
## read from JavaScript is always the global value.
## Type: String
# ===>
c.content.headers.accept_language = "en-US,en;q=0.9"

# <===  Custom headers for qutebrowser HTTP requests.
## Type: Dict
# ===>
c.content.headers.custom = {}

# <===  Value to send in the `DNT` header. When this is set to true,
## qutebrowser asks websites to not track your identity. If set to null,
## the DNT header is not sent at all.
## Type: Bool
# ===>
c.content.headers.do_not_track = True

# <===  When to send the Referer header. The Referer header tells websites
## from which website you were coming from when visiting them. Note that
## with QtWebEngine, websites can override this preference by setting the
## `Referrer-Policy:` header, so that any websites visited from them get
## the full referer. No restart is needed with QtWebKit.
## Type: String
## Valid values:
##   - always: Always send the Referer. With QtWebEngine 6.2+, this value is unavailable and will act like `same-domain`.
##   - never: Never send the Referer. This is not recommended, as some sites may break.
##   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites. With QtWebEngine, the referer will still be sent for other domains, but with stripped path information.
# ===>
c.content.headers.referer = "same-domain"

# <===  User agent to send.  The following placeholders are defined:  *
## `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
## The underlying WebKit version (set to a fixed value   with
## QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
## QtWebEngine. * `{qt_version}`: The underlying Qt version. *
## `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
## QtWebEngine. * `{upstream_browser_version}`: The corresponding
## Safari/Chrome version. * `{qutebrowser_version}`: The currently
## running qutebrowser version.  The default value is equal to the
## unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
## read from JavaScript is always the global value. With QtWebEngine
## between 5.12 and 5.14 (inclusive), changing the value exposed to
## JavaScript requires a restart.
## Type: FormatString
# ===>
c.content.headers.user_agent = "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}"
c.content.hyperlink_auditing = False  ## Enable hyperlink auditing (`<a ping>`).
c.content.images = True  ## Load images automatically in web pages.
c.content.javascript.alert = True  ## Show javascript alerts.
# c.content.javascript.can_close_tabs = False  ## Allow JavaScript to close tabs. #unavailable?
c.content.javascript.can_open_tabs_automatically = (
    False  ## Allow JavaScript to open new tabs without user interaction.
)

# <===  Allow JavaScript to read from or write to the clipboard. With
## QtWebEngine, writing the clipboard as response to a user interaction
## is always allowed.
## Type: String
## Valid values:
##   - none: Disable access to clipboard.
##   - access: Allow reading from and writing to the clipboard.
##   - access-paste: Allow accessing the clipboard and pasting clipboard content.
# ===>
c.content.javascript.clipboard = "none"

#
c.content.javascript.enabled = True  ## Enable JavaScript.

# <===  Enables the legacy touch event feature. This affects JS APIs such as:
## - ontouch* members on window, document, Element -
## document.createTouch, document.createTouchList -
## document.createEvent("TouchEvent") Newer Chromium versions have those
## disabled by default:
## https://bugs.chromium.org/p/chromium/issues/detail?id=392584
## https://groups.google.com/a/chromium.org/g/blink-dev/c/KV6kqDJpYiE
## Type: String
## Valid values:
##   - always: Legacy touch events are always enabled. This might cause some websites to assume a mobile device.
##   - auto: Legacy touch events are only enabled if a touch screen was detected on startup.
##   - never: Legacy touch events are always disabled.
# ===>
c.content.javascript.legacy_touch_events = "never"

# <===  Log levels to use for JavaScript console logging messages. When a
## JavaScript message with the level given in the dictionary key is
## logged, the corresponding dictionary value selects the qutebrowser
## logger to use. On QtWebKit, the "unknown" setting is always used. The
## following levels are valid: `none`, `debug`, `info`, `warning`,
## `error`.
## Type: Dict
# ===>
c.content.javascript.log = {
    "unknown": "debug",
    "info": "debug",
    "warning": "debug",
    "error": "debug",
}

# <===  Javascript messages to *not* show in the UI, despite a corresponding
## `content.javascript.log_message.levels` setting. Both keys and values
## are glob patterns, with the key matching the location of the error,
## and the value matching the error message. By default, the
## https://web.dev/csp/[Content security policy] violations triggered by
## qutebrowser's stylesheet handling are excluded, as those errors are to
## be expected and can't be easily handled by the underlying code.
## Type: Dict
# ===>
c.content.javascript.log_message.excludes = {
    "userscript:_qute_stylesheet": [
        "*Refused to apply inline style because it violates the following Content Security Policy directive: *"
    ]
}

# <===  Javascript message sources/levels to show in the qutebrowser UI. When
## a JavaScript message is logged from a location matching the glob
## pattern given in the key, and is from one of the levels listed as
## value, it's surfaced as a message in the qutebrowser UI. By default,
## errors happening in qutebrowser internally are shown to the user.
## Type: Dict
# ===>
c.content.javascript.log_message.levels = {
    "qute:*": ["error"],
    "userscript:GM-*": [],
    "userscript:*": ["error"],
}

# <===  Use the standard JavaScript modal dialog for `alert()` and
# ===>
c.content.javascript.modal_dialog = False  ## `confirm()`.

#
c.content.javascript.prompt = True  ## Show javascript prompts.
c.content.local_content_can_access_file_urls = (
    True  ## Allow locally loaded documents to access other local URLs.
)
c.content.local_content_can_access_remote_urls = (
    False  ## Allow locally loaded documents to access remote URLs.
)
c.content.local_storage = True  ## Enable support for HTML 5 local storage and Web SQL.
c.content.media.audio_capture = "ask"  ## Allow websites to record audio.
c.content.media.audio_video_capture = "ask"  ## Allow websites to record audio and video. Type: BoolAsk Valid values: true false ask
c.content.media.video_capture = (
    "ask"  ## Allow websites to record video. ## Type: BoolAsk
)
c.content.mouse_lock = "ask"  ## Allow websites to lock your mouse pointer.

# <===  Automatically mute tabs. Note that if the `:tab-mute` command is used,
## the mute status for the affected tab is now controlled manually, and
## this setting doesn't have any effect.
## Type: Bool
# ===>
c.content.mute = False
c.content.netrc_file = None  ## Netrc-file for HTTP authentication. If unset, `~/.netrc` is used. ## Type: File
c.content.notifications.enabled = (
    "ask"  ## Allow websites to show notifications. ## Type: BoolAsk
)

# <===  What notification presenter to use for web notifications. Note that
## not all implementations support all features of notifications: - The
## `qt` and `systray` options only support showing one notification at
## the time   and ignore the `tag` option to replace existing
## notifications. - The `herbe` option only supports showing one
## notification at the time and doesn't   show icons. - The `messages`
## option doesn't show icons and doesn't support the `click` and
## `close` events.
## Type: String
## Valid values:
##   - auto: Tries `libnotify`, `systray` and `messages`, uses the first one available without showing error messages.
##   - qt: Use Qt's native notification presenter, based on a system tray icon. Switching from or to this value requires a restart of qutebrowser.
##   - libnotify: Shows messages via DBus in a libnotify-compatible way. If DBus isn't available, falls back to `systray` or `messages`, but shows an error message.
##   - systray: Use a notification presenter based on a systray icon. Falls back to `libnotify` or `messages` if not systray is available. This is a reimplementation of the `qt` setting value, but with the possibility to switch to it at runtime.
##   - messages: Show notifications as qutebrowser messages. Most notification features aren't available.
##   - herbe: (experimental!) Show notifications using herbe (github.com/dudik/herbe). Most notification features aren't available.
# ===>
c.content.notifications.presenter = "auto"

# <===  Whether to show the origin URL for notifications. Note that URL
## patterns with this setting only get matched against the origin part of
## the URL, so e.g. paths in patterns will never match. Note that with
## the `qt` presenter, origins are never shown.
## Type: Bool
# ===>
c.content.notifications.show_origin = True

# <===  Display PDF files via PDF.js in the browser without showing a download
## prompt. Note that the files can still be downloaded by clicking the
## download button in the pdf.js viewer. With this set to `false`, the
## `:prompt-open-download --pdfjs` command (bound to `<Ctrl-p>` by
## default) can be used in the download prompt.
## Type: Bool
# ===>
c.content.pdfjs = True  # False
c.content.persistent_storage = "ask"  ## Allow websites to request persistent storage quota via `navigator.webkitPersistentStorage.requestQuota`.
c.content.plugins = False  ## Enable plugins in Web pages.

# <===  Request websites to minimize non-essentials animations and motion.
## This results in the `prefers-reduced-motion` CSS media query to
## evaluate to `reduce` (rather than `no-preference`). On Windows, if
## this setting is set to False, the system-wide animation setting is
## considered.
## Type: Bool
# ===>
c.content.prefers_reduced_motion = False
c.content.print_element_backgrounds = (
    True  ## Draw the background color and images also when the page is printed.
)
c.content.private_browsing = False  ## Open new windows in private browsing mode which does not record visited pages.

# <===  Proxy to use. In addition to the listed values, you can use a
## `socks://...` or `http://...` URL. Note that with QtWebEngine, it will
## take a couple of seconds until the change is applied, if this value is
## changed at runtime. Authentication for SOCKS proxies isn't supported
## due to Chromium limitations.
## Type: Proxy
## Valid values:
##   - system: Use the system wide proxy.
##   - none: Don't use any proxy
# ===>
c.content.proxy = "system"
# c.content.proxy_dns_requests = True  ## Send DNS requests over the configured proxy. #unavailable?
c.content.register_protocol_handler = "ask"  ## Allow websites to register protocol handlers via `navigator.registerProtocolHandler`. Type: BoolAsk
c.content.site_specific_quirks.enabled = True  ## Enable quirks (such as faked user agent headers) needed to get specific sites to work properly.

# <===  Disable a list of named quirks.
## Type: FlagList
## Valid values:
##   - ua-whatsapp
##   - ua-google
##   - ua-slack
##   - ua-googledocs
##   - js-whatsapp-web
##   - js-discord
##   - js-string-replaceall
##   - js-array-at
##   - misc-krunker
##   - misc-mathml-darkmode
# ===>
c.content.site_specific_quirks.skip = []

# <===  How to proceed on TLS certificate errors.
## Type: String
## Valid values:
##   - ask: Ask how to proceed for every certificate error (unless non-overridable due to HSTS).
##   - ask-block-thirdparty: Ask how to proceed for normal page loads, but silently block resource loads.
##   - block: Automatically block loading on certificate errors.
##   - load-insecurely: Force loading pages despite certificate errors. This is *insecure* and should be avoided. Instead of using this, consider fixing the underlying issue or importing a self-signed certificate via `certutil` (or Chromium) instead.
# ===>
c.content.tls.certificate_errors = "ask"

# <===  How navigation requests to URLs with unknown schemes are handled.
## Type: String
## Valid values:
##   - disallow: Disallows all navigation requests to URLs with unknown schemes.
##   - allow-from-user-interaction: Allows navigation requests to URLs with unknown schemes that are issued from user-interaction (like a mouse-click), whereas other navigation requests (for example from JavaScript) are suppressed.
##   - allow-all: Allows all navigation requests to URLs with unknown schemes.
# ===>
c.content.unknown_url_scheme_policy = "allow-from-user-interaction"

# <===  List of user stylesheet filenames to use.
## Type: List of File, or File
# ===>
c.content.user_stylesheets = []
c.content.webgl = True  ## Enable WebGL.

# <===  Which interfaces to expose via WebRTC.
## Type: String
## Valid values:
##   - all-interfaces: WebRTC has the right to enumerate all interfaces and bind them to discover public interfaces.
##   - default-public-and-private-interfaces: WebRTC should only use the default route used by http. This also exposes the associated default private address. Default route is the route chosen by the OS on a multi-homed endpoint.
##   - default-public-interface-only: WebRTC should only use the default route used by http. This doesn't expose any local addresses.
##   - disable-non-proxied-udp: WebRTC should only use TCP to contact peers or servers unless the proxy server supports UDP. This doesn't expose any local addresses either.
# ===>
c.content.webrtc_ip_handling_policy = "all-interfaces"

# <===  Monitor load requests for cross-site scripting attempts. Suspicious
## scripts will be blocked and reported in the devtools JavaScript
## console. Note that bypasses for the XSS auditor are widely known and
## it can be abused for cross-site info leaks in some scenarios, see:
## https://www.chromium.org/developers/design-documents/xss-auditor
## Type: Bool
# ===>
c.content.xss_auditing = False

# --------------------------------------------
#                    DOWNLOADS
# --------------------------------------------
c.downloads.location.directory = "~/Downloads"  ## Directory to save downloads to. If unset, a sensible OS-specific default is used.
c.downloads.location.prompt = True  # Prompt the user for the download location. If set to false,`downloads.location.directory` will be used.
c.downloads.location.remember = True  ## Remember the last used download directory.

# <===  What to display in the download filename input.
## Type: String
## Valid values:
##   - path: Show only the download path.
##   - filename: Show only download filename.
##   - both: Show download path and filename.
# ===>
c.downloads.location.suggestion = "both"

# <===  Default program used to open downloads. If null, the default internal
## handler is used. Any `{}` in the string will be expanded to the
## filename, else the filename will be appended.
## Type: String
# ===>
c.downloads.open_dispatcher = None

c.downloads.position = (
    "top"  ## Where to show the downloaded files. ## Valid values:  - top - bottom
)

# <===  Automatically abort insecure (HTTP) downloads originating from secure
## (HTTPS) pages. For per-domain settings, the relevant URL is the URL
## initiating the download, not the URL the download itself is coming
## from. It's not recommended to set this setting to false globally.
## Type: Bool
# ===>
c.downloads.prevent_mixed_content = True
c.downloads.remove_finished = 5000  ## Duration (in milliseconds) to wait before removing finished downloads. If set to -1, downloads are never removed.
#

# <===  Editor (and arguments) to use for the `edit-*` commands. The following
## placeholders are defined:  * `{file}`: Filename of the file to be
## edited. * `{line}`: Line in which the caret is found in the text. *
## `{column}`: Column in which the caret is found in the text. *
## `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
## Same as `{column}`, but starting from index 0.
## Type: ShellCommand TODO
# ===>
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

#
c.editor.encoding = "utf-8"  ## Encoding to use for the editor.
c.editor.remove_file = True  ## Delete the temporary file upon closing the editor.

# <===  Command (and arguments) to use for selecting a single folder in forms.
## The command should write the selected folder path to the specified
## file or stdout. The following placeholders are defined: * `{}`:
## Filename of the file to be written to. If not contained in any
## argument, the   standard output of the command is read instead.
## Type: ShellCommand
# ===>
c.fileselect.folder.command = [
    "alacritty",
    "-e",
    "ranger",
    "--show-only-dirs",
    "--choosedir={}",
]

# <===  Handler for selecting file(s) in forms. If `external`, then the
## commands specified by `fileselect.single_file.command`,
## `fileselect.multiple_files.command` and `fileselect.folder.command`
## are used to select one file, multiple files, and folders,
## respectively.
## Type: String
## Valid values:
##   - default: Use the default file selector.
##   - external: Use an external command.
# ===>
c.fileselect.handler = "external"

# <===  Command (and arguments) to use for selecting multiple files in forms.
## The command should write the selected file paths to the specified file
## or to stdout, separated by newlines. The following placeholders are
## defined: * `{}`: Filename of the file to be written to. If not
## contained in any argument, the   standard output of the command is
## read instead.
## Type: ShellCommand
# ===>
c.fileselect.multiple_files.command = ["alacritty", "-e", "ranger", "--choosefiles={}"]

# <===  Command (and arguments) to use for selecting a single file in forms.
## The command should write the selected file path to the specified file
## or stdout. The following placeholders are defined: * `{}`: Filename of
## the file to be written to. If not contained in any argument, the
## standard output of the command is read instead.
## Type: ShellCommand
# ===>
c.fileselect.single_file.command = ["alacritty", "-e", "ranger", "--choosefile={}"]

# --------------------------------------------
#                    FONTS
# --------------------------------------------
# <===  Default font families to use. Whenever "default_family" is used in a
## font setting, it's replaced with the fonts listed here. If set to an
## empty value, a system-specific monospace default is used.
## Type: List of Font, or Font
# ===>
c.fonts.default_family = ["Iosevka Nerd Font"]
# <===  Font used in the completion categories.
## Type: Font
# ===>
c.fonts.completion.category = "bold default_size default_family"
# <===  Font used in the completion widget.
## Type: Font
# ===>
c.fonts.completion.entry = "default_size default_family"
# <===  Font used for the context menu. If set to null, the Qt default is
## used.
## Type: Font
# ===>
c.fonts.contextmenu = "default_size default_family"
# <===  Font used for the debugging console.
## Type: Font
# ===>
c.fonts.debug_console = "default_size default_family"
# <===  Default font size to use. Whenever "default_size" is used in a font
## setting, it's replaced with the size listed here. Valid values are
## either a float value with a "pt" suffix, or an integer value with a
## "px" suffix.
## Type: String
# ===>
c.fonts.default_size = "12pt"
# <===  Font used for the downloadbar.
## Type: Font
# ===>
c.fonts.downloads = "default_size default_family"
# <===  Font used for the hints.
## Type: Font
# ===>
c.fonts.hints = "bold default_size default_family"
# <===  Font used in the keyhint widget.
## Type: Font
# ===>
c.fonts.keyhint = "default_size default_family"
# <===  Font used for error messages.
## Type: Font
# ===>
c.fonts.messages.error = "default_size default_family"
# <===  Font used for info messages.
## Type: Font
# ===>
c.fonts.messages.info = "default_size default_family"
# <===  Font used for warning messages.
## Type: Font
# ===>
c.fonts.messages.warning = "default_size default_family"
# <===  Font used for prompts.
## Type: Font
# ===>
c.fonts.prompts = "default_size sans-serif"
# <===  Font used in the statusbar.
## Type: Font
# ===>
c.fonts.statusbar = "default_size default_family"
# <===  Font used for selected tabs.
## Type: Font
# ===>
c.fonts.tabs.selected = "default_size default_family"
# <===  Font used for unselected tabs.
## Type: Font
# ===>
c.fonts.tabs.unselected = "default_size default_family"
# <===  Font used for tooltips. If set to null, the Qt default is used.
## Type: Font
# ===>
c.fonts.tooltip = "default_size default_family"
# <===  Font family for cursive fonts.
## Type: FontFamily
# ===>
c.fonts.web.family.cursive = "Iosevka Nerd Font"
# <===  Font family for fantasy fonts.
## Type: FontFamily
# ===>
c.fonts.web.family.fantasy = "Iosevka Nerd Font"
# <===  Font family for fixed fonts.
## Type: FontFamily
# ===>
c.fonts.web.family.fixed = "Iosevka Nerd Font"
# <===  Font family for sans-serif fonts.
## Type: FontFamily
# ===>
c.fonts.web.family.sans_serif = "Iosevka Nerd Font"
# <===  Font family for serif fonts.
## Type: FontFamily
# ===>
c.fonts.web.family.serif = "Iosevka Nerd Font"
# <===  Font family for standard fonts.
## Type: FontFamily
# ===>
c.fonts.web.family.standard = "Iosevka Nerd Font"
# <===  Default font size (in pixels) for regular text.
## Type: Int
# ===>
c.fonts.web.size.default = 16
# <===  Default font size (in pixels) for fixed-pitch text.
## Type: Int
# ===>
c.fonts.web.size.default_fixed = 13
# <===  Hard minimum font size (in pixels).
## Type: Int
# ===>
c.fonts.web.size.minimum = 0
# <===  Minimum logical font size (in pixels) that is applied when zooming
## out.
## Type: Int
# ===>
c.fonts.web.size.minimum_logical = 6


# --------------------------------------------
#                    HINTS
# --------------------------------------------
# <===  When a hint can be automatically followed without pressing Enter.
## Type: String
## Valid values:
##   - always: Auto-follow whenever there is only a single hint on a page.
##   - unique-match: Auto-follow whenever there is a unique non-empty match in either the hint string (word mode) or filter (number mode).
##   - full-match: Follow the hint when the user typed the whole hint (letter, word or number mode) or the element's text (only in number mode).
##   - never: The user will always need to press Enter to follow a hint.
# ===>
c.hints.auto_follow = "unique-match"

# <===  Duration (in milliseconds) to ignore normal-mode key bindings after a
## successful auto-follow.
## Type: Int
# ===>
c.hints.auto_follow_timeout = 0

#
c.hints.border = "1px solid #d0a215"  ## CSS border value for hints.

# <===  Characters used for hint strings. ## Type: UniqueCharString
# ===>
c.hints.chars = "asdfghjkl"

# <===  Dictionary file to be used by the word hints. ## Type: File
# ===>
c.hints.dictionary = "/usr/share/dict/words"

# <===  Which implementation to use to find elements to hint.
## Type: String
## Valid values:
##   - javascript: Better but slower
##   - python: Slightly worse but faster
# ===>
# c.hints.find_implementation = "python" #unavailable?

# <===  Hide unmatched hints in rapid mode.
## Type: Bool
# ===>
c.hints.hide_unmatched_rapid_hints = True
c.hints.leave_on_load = False  ## Leave hint mode when starting a new page load.
c.hints.min_chars = 1  ## Minimum number of characters used for hint strings.

# <===  Mode to use for hints.
## Type: String
## Valid values:
##   - number: Use numeric hints. (In this mode you can also type letters from the hinted element to filter and reduce the number of elements that are hinted.)
##   - letter: Use the characters in the `hints.chars` setting.
##   - word: Use hints words based on the html elements and the extra words.
# ===>
c.hints.mode = "letter"

# <===  Comma-separated list of regular expressions to use for 'next' links.
## Type: List of Regex
# ===>
c.hints.next_regexes = [
    "\\bnext\\b",
    "\\bmore\\b",
    "\\bnewer\\b",
    "\\b[>→≫]\\b",
    "\\b(>>|»)\\b",
    "\\bcontinue\\b",
]

# <===  Padding (in pixels) for hints.
## Type: Padding
# ===>
c.hints.padding = {"top": 0, "bottom": 0, "left": 3, "right": 3}

# <===  Comma-separated list of regular expressions to use for 'prev' links.
## Type: List of Regex
# ===>
c.hints.prev_regexes = [
    "\\bprev(ious)?\\b",
    "\\bback\\b",
    "\\bolder\\b",
    "\\b[<←≪]\\b",
    "\\b(<<|«)\\b",
]

# <===  Rounding radius (in pixels) for the edges of hints.
## Type: Int
# ===>
c.hints.radius = 6
c.hints.scatter = True  ## Scatter hint key chains (like Vimium) or not (like dwb). Ignored for number hints.

# <===  CSS selectors used to determine which elements on a page should have
## hints.
## Type: Dict
# ===>
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

# <===  Maximum time (in minutes) between two history items for them to be
## considered being from the same browsing session. Items with less time
## between them are grouped when being displayed in `:history`. Use -1 to
## disable separation.
## Type: Int
# ===>
c.history_gap_interval = 30

# --------------------------------------------
#                    INPUT
# --------------------------------------------
c.input.escape_quits_reporter = True  ## Allow Escape to quit the crash reporter.

# <===  Which unbound keys to forward to the webview in normal mode.
## Type: String
## Valid values:
##   - all: Forward all unbound keys.
##   - auto: Forward unbound non-alphanumeric keys.
##   - none: Don't forward any keys.
# ===>
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
# <===  Timeout (in milliseconds) for partially typed key bindings. If the
## current input forms only partial matches, the keystring will be
## cleared after this time. If set to 0, partially typed bindings are
## never cleared.
## Type: Int
# ===>
c.input.partial_timeout = 0

# <===  Enable spatial navigation. Spatial navigation consists in the ability
## to navigate between focusable elements, such as hyperlinks and form
## controls, on a web page by using the Left, Right, Up and Down arrow
## keys. For example, if a user presses the Right key, heuristics
## determine whether there is an element they might be trying to reach
## towards the right and which element they probably want.
## Type: Bool
# ===>
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

# <===  How to open links in an existing instance if a new one is launched.
## This happens when e.g. opening a link from a terminal. See
## `new_instance_open_target_window` to customize in which window the
## link is opened in.
## Type: String
## Valid values:
##   - tab: Open a new tab in the existing window and activate the window.
##   - tab-bg: Open a new background tab in the existing window and activate the window.
##   - tab-silent: Open a new tab in the existing window without activating the window.
##   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
##   - window: Open in a new window.
##   - private-window: Open in a new private window.
# ===>
c.new_instance_open_target = "window"  # tab

# <===  Which window to choose when opening links as new tabs. When
## `new_instance_open_target` is set to `window`, this is ignored.
## Type: String
## Valid values:
##   - first-opened: Open new tabs in the first (oldest) opened window.
##   - last-opened: Open new tabs in the last (newest) opened window.
##   - last-focused: Open new tabs in the most recently focused window.
##   - last-visible: Open new tabs in the most recently visible window.
# ===>
c.new_instance_open_target_window = "last-focused"
c.prompt.filebrowser = True  ## Show a filebrowser in download prompts.
c.prompt.radius = 8  ## Rounding radius (in pixels) for the edges of prompts.

# --------------------------------------------
#                 QT
# --------------------------------------------
# <===  Additional arguments to pass to Qt, without leading `--`. With
## QtWebEngine, some Chromium arguments (see
## https://peter.sh/experiments/chromium-command-line-switches/ for a
## list) will work.
## Type: List of String
# ===>
c.qt.args = []

# <===  Enables Web Platform features that are in development. This passes the
## `--enable-experimental-web-platform-features` flag to Chromium. By
## default, this is enabled with Qt 5 to maximize compatibility despite
## an aging Chromium base.
## Type: String
## Valid values:
##   - always: Enable experimental web platform features.
##   - auto: Enable experimental web platform features when using Qt 5.
##   - never: Disable experimental web platform features.
# ===>
c.qt.chromium.experimental_web_platform_features = "auto"

# <===  When to use Chromium's low-end device mode. This improves the RAM
## usage of renderer processes, at the expense of performance.
## Type: String
## Valid values:
##   - always: Always use low-end device mode.
##   - auto: Decide automatically (uses low-end mode with < 1 GB available RAM).
##   - never: Never use low-end device mode.
# ===>
c.qt.chromium.low_end_device_mode = "auto"

# <===  Which Chromium process model to use. Alternative process models use
## less resources, but decrease security and robustness. See the
## following pages for more details:    -
## https://www.chromium.org/developers/design-documents/process-models
## - https://doc.qt.io/qt-6/qtwebengine-features.html#process-models
## Type: String
## Valid values:
##   - process-per-site-instance: Pages from separate sites are put into separate processes and separate visits to the same site are also isolated.
##   - process-per-site: Pages from separate sites are put into separate processes. Unlike Process per Site Instance, all visits to the same site will share an OS process. The benefit of this model is reduced memory consumption, because more web pages will share processes. The drawbacks include reduced security, robustness, and responsiveness.
##   - single-process: Run all tabs in a single process. This should be used for debugging purposes only, and it disables `:open --private`.
# ===>
c.qt.chromium.process_model = "process-per-site-instance"

# <===  What sandboxing mechanisms in Chromium to use. Chromium has various
## sandboxing layers, which should be enabled for normal browser usage.
## Mainly for testing and development, it's possible to disable
## individual sandboxing layers via this setting. Open `chrome://sandbox`
## to see the current sandbox status. Changing this setting is only
## recommended if you know what you're doing, as it **disables one of
## Chromium's security layers**. To avoid sandboxing being accidentally
## disabled persistently, this setting can only be set via `config.py`,
## not via `:set`. See the Chromium documentation for more details: - htt
## ps://chromium.googlesource.com/chromium/src/\+/HEAD/docs/linux/sandbox
## ing.md[Linux] - https://chromium.googlesource.com/chromium/src/\+/HEAD
## /docs/design/sandbox.md[Windows] - https://chromium.googlesource.com/c
## hromium/src/\+/HEAD/docs/design/sandbox_faq.md[FAQ (Windows-centric)]
## Type: String
## Valid values:
##   - enable-all: Enable all available sandboxing mechanisms.
##   - disable-seccomp-bpf: Disable the Seccomp BPF filter sandbox (Linux only).
##   - disable-all: Disable all sandboxing (**not recommended!**).
# ===>
c.qt.chromium.sandboxing = "enable-all"

# <===  Additional environment variables to set. Setting an environment
## variable to null/None will unset it.
## Type: Dict
# ===>
c.qt.environ = {}

# <===  Force a Qt platform to use. This sets the `QT_QPA_PLATFORM`
## environment variable and is useful to force using the XCB plugin when
## running QtWebEngine on Wayland.
## Type: String
# ===>
c.qt.force_platform = None

# <===  Force a Qt platformtheme to use. This sets the `QT_QPA_PLATFORMTHEME`
## environment variable which controls dialogs like the filepicker. By
## default, Qt determines the platform theme based on the desktop
## environment.
## Type: String
# ===>
c.qt.force_platformtheme = None

# <===  Force software rendering for QtWebEngine. This is needed for
## QtWebEngine to work with Nouveau drivers and can be useful in other
## scenarios related to graphic issues.
## Type: String
## Valid values:
##   - software-opengl: Tell LibGL to use a software implementation of GL (`LIBGL_ALWAYS_SOFTWARE` / `QT_XCB_FORCE_SOFTWARE_OPENGL`)
##   - qt-quick: Tell Qt Quick to use a software renderer instead of OpenGL. (`QT_QUICK_BACKEND=software`)
##   - chromium: Tell Chromium to disable GPU support and use Skia software rendering instead. (`--disable-gpu`)
##   - none: Don't force software rendering.
# ===>
c.qt.force_software_rendering = "none"

# <===  Turn on Qt HighDPI scaling. This is equivalent to setting
## QT_ENABLE_HIGHDPI_SCALING=1 (Qt >= 5.14) in the environment. It's off
## by default as it can cause issues with some bitmap fonts. As an
## alternative to this, it's possible to set font sizes and the
## `zoom.default` setting.
## Type: Bool
# ===>
c.qt.highdpi = False

# <===  Disable accelerated 2d canvas to avoid graphical glitches. On some
## setups graphical issues can occur on sites like Google sheets and
## PDF.js. These don't occur when accelerated 2d canvas is turned off, so
## we do that by default. So far these glitches only occur on some Intel
## graphics devices.
## Type: String
## Valid values:
##   - always: Disable accelerated 2d canvas
##   - auto: Disable on Qt6 < 6.6.0, enable otherwise
##   - never: Enable accelerated 2d canvas
# ===>
c.qt.workarounds.disable_accelerated_2d_canvas = "auto"

# <===  Work around locale parsing issues in QtWebEngine 5.15.3. With some
## locales, QtWebEngine 5.15.3 is unusable without this workaround. In
## affected scenarios, QtWebEngine will log "Network service crashed,
## restarting service." and only display a blank page. However, It is
## expected that distributions shipping QtWebEngine 5.15.3 follow up with
## a proper fix soon, so it is disabled by default.
## Type: Bool
# ===>
c.qt.workarounds.locale = False

# <===  Delete the QtWebEngine Service Worker directory on every start. This
## workaround can help with certain crashes caused by an unknown
## QtWebEngine bug related to Service Workers. Those crashes happen
## seemingly immediately on Windows; after one hour of operation on other
## systems. Note however that enabling this option *can lead to data
## loss* on some pages (as Service Worker data isn't persisted) and will
## negatively impact start-up time.
## Type: Bool
# ===>
c.qt.workarounds.remove_service_workers = False

# <===  When/how to show the scrollbar.
## Type: String
## Valid values:
##   - always: Always show the scrollbar.
##   - never: Never show the scrollbar.
##   - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
##   - overlay: Show an overlay scrollbar. On macOS, this is unavailable and equal to `when-searching`; with the QtWebKit backend, this is equal to `never`. Enabling/disabling overlay scrollbars requires a restart.
# ===>
c.scrolling.bar = "never"

# <===  Enable smooth scrolling for web pages. Note smooth scrolling does not
## work with the `:scroll-px` command.
## Type: Bool
# ===>
c.scrolling.smooth = False

## When to find text on a page case-insensitively.
## Type: IgnoreCase
## Valid values:
##   - always: Search case-insensitively.
##   - never: Search case-sensitively.
##   - smart: Search case-sensitively if there are capital characters.
# ===>
c.search.ignore_case = "smart"
c.search.incremental = True  ## Find text on a page incrementally, renewing the search for each typed character.
c.search.wrap = True  ## Wrap around at the top and bottom of the page when advancing through ## text matches using `:search-next` and `:search-prev`.
c.search.wrap_messages = True  ## Display messages when advancing through text matches at the top and bottom of the page, e.g. `Search hit TOP`.
c.session.default_name = "default"  ## Name of the session to save by default. If this is set to null, the session which was last loaded is saved. ## Type: SessionName
c.session.lazy_restore = False  ## Load a restored tab as soon as it takes focus.

# <===  Languages to use for spell checking. You can check for available
## languages and install dictionaries using scripts/dictcli.py. Run the
## script with -h/--help for instructions.
## Type: List of String
## Valid values:
##   - af-ZA: Afrikaans (South Africa)
##   - bg-BG: Bulgarian (Bulgaria)
##   - ca-ES: Catalan (Spain)
##   - cs-CZ: Czech (Czech Republic)
##   - da-DK: Danish (Denmark)
##   - de-DE: German (Germany)
##   - el-GR: Greek (Greece)
##   - en-AU: English (Australia)
##   - en-CA: English (Canada)
##   - en-GB: English (United Kingdom)
##   - en-US: English (United States)
##   - es-ES: Spanish (Spain)
##   - et-EE: Estonian (Estonia)
##   - fa-IR: Farsi (Iran)
##   - fo-FO: Faroese (Faroe Islands)
##   - fr-FR: French (France)
##   - he-IL: Hebrew (Israel)
##   - hi-IN: Hindi (India)
##   - hr-HR: Croatian (Croatia)
##   - hu-HU: Hungarian (Hungary)
##   - id-ID: Indonesian (Indonesia)
##   - it-IT: Italian (Italy)
##   - ko: Korean
##   - lt-LT: Lithuanian (Lithuania)
##   - lv-LV: Latvian (Latvia)
##   - nb-NO: Norwegian (Norway)
##   - nl-NL: Dutch (Netherlands)
##   - pl-PL: Polish (Poland)
##   - pt-BR: Portuguese (Brazil)
##   - pt-PT: Portuguese (Portugal)
##   - ro-RO: Romanian (Romania)
##   - ru-RU: Russian (Russia)
##   - sh: Serbo-Croatian
##   - sk-SK: Slovak (Slovakia)
##   - sl-SI: Slovenian (Slovenia)
##   - sq: Albanian
##   - sr: Serbian
##   - sv-SE: Swedish (Sweden)
##   - ta-IN: Tamil (India)
##   - tg-TG: Tajik (Tajikistan)
##   - tr-TR: Turkish (Turkey)
##   - uk-UA: Ukrainian (Ukraine)
##   - vi-VN: Vietnamese (Viet Nam)
# ===>
c.spellcheck.languages = ["en-US", "en-GB", "fr-FR"]

# <===  Padding (in pixels) for the statusbar.
## Type: Padding
# ===>
c.statusbar.padding = {"top": 1, "bottom": 1, "left": 0, "right": 0}
c.statusbar.position = (
    "bottom"  ## Position of the status bar. ## Valid values:  - top  - bottom
)

# <===  When to show the statusbar.
## Type: String
## Valid values:
##   - always: Always show the statusbar.
##   - never: Always hide the statusbar.
##   - in-mode: Show the statusbar when in modes other than normal mode.
# ===>
c.statusbar.show = "always"

# <===  List of widgets displayed in the statusbar.
## Type: List of StatusbarWidget
## Valid values:
##   - url: Current page URL.
##   - scroll: Percentage of the current page position like `10%`.
##   - scroll_raw: Raw percentage of the current page position like `10`.
##   - history: Display an arrow when possible to go back/forward in history.
##   - search_match: A match count when searching, e.g. `Match [2/10]`.
##   - tabs: Current active tab, e.g. `2`.
##   - keypress: Display pressed keys when composing a vi command.
##   - progress: Progress bar for the current page loading.
##   - text:foo: Display the static text after the colon, `foo` in the example.
##   - clock: Display current time. The format can be changed by adding a format string via `clock:...`. For supported format strings, see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes[the Python datetime documentation].
# ===>
c.statusbar.widgets = [
    "keypress",
    "url",
    "scroll",
    "history",
    "tabs",
    "search_match",
    "progress",
]

##--------------------------------------------
##                  TABS
##--------------------------------------------
#
c.tabs.background = True  ## Open new tabs (middleclick/ctrl+click) in the background.
c.tabs.close_mouse_button = "middle"  ## Mouse button with which to close tabs. ## Valid values: ##   - right: Close tabs on right-click. ##   - middle: Close tabs on middle-click. ##   - none: Don't close tabs using the mouse.

# <===  How to behave when the close mouse button is pressed on the tab bar.
## Type: String
## Valid values:
##   - new-tab: Open a new tab.
##   - close-current: Close the current tab.
##   - close-last: Close the last tab.
##   - ignore: Don't do anything.
# ===>
c.tabs.close_mouse_button_on_bar = "new-tab"
c.tabs.favicons.scale = 0.8  ## Scaling factor for favicons in the tab bar. The tab size is unchanged, so big favicons also require extra `tabs.padding`.
c.tabs.favicons.show = "always"  ## Valid values: ##   - always: Always show favicons. ##   - never: Always hide favicons. ##   - pinned: Show favicons only on pinned tabs.
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

# <===  How to behave when the last tab is closed. If the
## `tabs.tabs_are_windows` setting is set, this is ignored and the
## behavior is always identical to the `close` value.
## Type: String
## Valid values:
##   - ignore: Don't do anything.
##   - blank: Load a blank page.
##   - startpage: Load the start page.
##   - default-page: Load the default page.
##   - close: Close the window.
# ===>
c.tabs.last_close = "ignore"

# <===  Maximum width (in pixels) of tabs (-1 for no maximum). This setting
## only applies when tabs are horizontal. This setting does not apply to
## pinned tabs, unless `tabs.pinned.shrink` is False. This setting may
## not apply properly if max_width is smaller than the minimum size of
## tab contents, or smaller than tabs.min_width.
## Type: Int
# ===>
c.tabs.max_width = -1

# <===  Minimum width (in pixels) of tabs (-1 for the default minimum size
## behavior). This setting only applies when tabs are horizontal. This
## setting does not apply to pinned tabs, unless `tabs.pinned.shrink` is
## False.
## Type: Int
# ===>
c.tabs.min_width = -1

# <===  When switching tabs, what input mode is applied.
## Type: String
## Valid values:
##   - persist: Retain the current mode.
##   - restore: Restore previously saved mode.
##   - normal: Always revert to normal mode.
# ===>
c.tabs.mode_on_change = "normal"
c.tabs.mousewheel_switching = True  ## Switch between tabs using the mouse wheel.

# <===  Position of new tabs opened from another tab. See
## `tabs.new_position.stacking` for controlling stacking behavior.
## Type: NewTabPosition
## Valid values: prev: Before the current tab. next: After the current tab. first: At the beginning. last: At the end.
# ===>
c.tabs.new_position.related = "next"

# <===  Stack related tabs on top of each other when opened consecutively.
## Only applies for `next` and `prev` values of
## `tabs.new_position.related` and `tabs.new_position.unrelated`.
## Type: Bool
# ===>
c.tabs.new_position.stacking = True

# <===  Position of new tabs which are not opened from another tab. See
## `tabs.new_position.stacking` for controlling stacking behavior.
## Type: NewTabPosition
## Valid values: prev: Before the current tab. next: After the current tab. first: At the beginning. last: At the end.
# ===>
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

# <===  Which tab to select when the focused tab is removed.
## Type: SelectOnRemove
## Valid values:
##   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
##   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
##   - last-used: Select the previously selected tab.
# ===>
c.tabs.select_on_remove = "next"

# <===  When to show the tab bar.
## Type: String
## Valid values:
##   - always: Always show the tab bar.
##   - never: Always hide the tab bar.
##   - multiple: Hide the tab bar if only one tab is open.
##   - switching: Show the tab bar when switching tabs.
# ===>
c.tabs.show = "always"

c.tabs.show_switching_delay = 800  ## Duration (in milliseconds) to show the tab bar before hiding it when tabs.show is set to 'switching'.

c.tabs.tabs_are_windows = False  ## Open a new window for every tab.

c.tabs.title.alignment = (
    "left"  ## Alignment of the text inside of tabs. Valid values: left right center
)

c.tabs.title.elide = "right"  ## Position of ellipsis in truncated title of tabs. ## Valid values: left right middle none

# <===  Format to use for the tab title. The following placeholders are
## defined:  * `{perc}`: Percentage as a string like `[10%]`. *
## `{perc_raw}`: Raw percentage, e.g. `10`. * `{current_title}`: Title of
## the current web page. * `{title_sep}`: The string `" - "` if a title
## is set, empty otherwise. * `{index}`: Index of this tab. *
## `{aligned_index}`: Index of this tab padded with spaces to have the
## same   width. * `{relative_index}`: Index of this tab relative to the
## current tab. * `{id}`: Internal tab ID of this tab. * `{scroll_pos}`:
## Page scroll position. * `{host}`: Host of the current web page. *
## `{backend}`: Either `webkit` or `webengine` * `{private}`: Indicates
## when private mode is enabled. * `{current_url}`: URL of the current
## web page. * `{protocol}`: Protocol (http/https/...) of the current web
## page. * `{audio}`: Indicator for audio/mute status.
## Type: FormatString
# ===>
c.tabs.title.format = "{private}{audio}{index}: {current_title} {title_sep} {host}"

# <===  Format to use for the tab title for pinned tabs. The same placeholders
## like for `tabs.title.format` are defined.
## Type: FormatString
# ===>
c.tabs.title.format_pinned = "{index}"
c.tabs.tooltips = True  ## Show tooltips on tabs. Note this setting only affects windows opened# after it has been set.
c.tabs.undo_stack_size = (
    -1
)  ## Number of closed tabs (per window) and closed windows to remember for :undo (-1 for no maximum).
c.tabs.width = "15%"  ## Width (in pixels or as percentage of the window) of the tab bar if it's vertical. ## Type: PercOrInt
c.tabs.wrap = True  ## Wrap when changing tabs.

# <===  What search to start when something else than a URL is entered.
## Type: String
## Valid values:
##   - naive: Use simple/naive check.
##   - dns: Use DNS requests (might be slow!).
##   - never: Never search automatically.
##   - schemeless: Always search automatically unless URL explicitly contains a scheme.
# ===>
c.url.auto_search = "naive"

# <===  Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
## for a blank page.
## Type: FuzzyUrl
# ===>
c.url.default_page = "https://start.duckduckgo.com/"

# <===  URL segments where `:navigate increment/decrement` will search for a
## number.
## Type: FlagList
## Valid values:
##   - host
##   - port
##   - path
##   - query
##   - anchor
# ===>
c.url.incdec_segments = ["path", "query"]

# <===  Open base URL of the searchengine if a searchengine shortcut is
## invoked without parameters.
## Type: Bool
# ===>
c.url.open_base_url = True

# <===  Search engines which can be used via the address bar.  Maps a search
## engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
## placeholder. The placeholder will be replaced by the search term, use
## `{{` and `}}` for literal `{`/`}` braces.  The following further
## placeholds are defined to configure how special characters in the
## search terms are replaced by safe characters (called 'quoting'):  *
## `{}` and `{semiquoted}` quote everything except slashes; this is the
## most   sensible choice for almost all search engines (for the search
## term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
## * `{quoted}` quotes all characters (for `slash/and&amp` this
## placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
## nothing (for `slash/and&amp` this placeholder   expands to
## `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
## multiple times.  The search engine named `DEFAULT` is used when
## `url.auto_search` is turned on and something else than a URL was
## entered to be opened. Other search engines can be used by prepending
## the search engine name to the search term, e.g. `:open google
## qutebrowser`.
## Type: Dict
# ===>
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "¿g": "https://google.com/search?q={}",
    "¿w": "https://en.wikipedia.org/w/index.php?search={}",
    "¿py": "https://docs.python.org/3/search.html?q={}",
    "¿doi": "https://dx.doi.org/{}",
    "¿arch": "https://wiki.archlinux.org/title/Special:Search/{}",
    "¿ð": "https://www.ncbi.nlm.nih.gov/search/all/?term={}",
    "¿ðc": "https://pubchem.ncbi.nlm.nih.gov/#query={}",
    "¿ðp": "https://pubmed.ncbi.nlm.nih.gov/?term={}",
    "¿ðm": "https://www.ncbi.nlm.nih.gov/mesh/?term={}",
    "¿trials": "https://clinicaltrials.gov/search?term={}&viewType=Table",
    "¿gh": "https://github.com/search?q={}&type=repositories",
    "¿docs": "https://{}.readthedocs.io/en/latest/index.html",
}

# <===  Page(s) to open at the start.
## Type: List of FuzzyUrl, or FuzzyUrl
# ===>
c.url.start_pages = ["https://start.duckduckgo.com"]

# <===  URL parameters to strip with `:yank url`.
## Type: List of String
# ===>
c.url.yank_ignored_parameters = [
    "ref",
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "utm_name",
]

# <===  Hide the window decoration.  This setting requires a restart on
## Wayland.
## Type: Bool
# ===>
c.window.hide_decoration = True  # False

# <===  Format to use for the window title. The same placeholders like for
## `tabs.title.format` are defined.
## Type: FormatString
# ===>
c.window.title_format = "{perc}{current_title}{title_sep}qutebrowser"

# <===  Set the main window background to transparent.  This allows having a
## transparent tab- or statusbar (might require a compositor such as
## picom). However, it breaks some functionality such as dmenu embedding
## via its `-w` option. On some systems, it was additionally reported
## that main window transparency negatively affects performance.  Note
## this setting only affects windows opened after setting it.
## Type: Bool
# ===>
c.window.transparent = True
c.zoom.default = "100%"  ## Default zoom level.

# <===  Available zoom levels.
## Type: List of Perc
# ===>
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
# c.zoom.text_only = ( #unavailable?
# False  ## Apply the zoom factor on a frame only to the text or to all content.
# )
