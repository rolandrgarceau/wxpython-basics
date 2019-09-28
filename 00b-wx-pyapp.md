# [wx.PyApp](https://wxpython.org/Phoenix/docs/html/wx.PyApp.html)

The wx.App class represents the application itself when USE_GUI=1.

In addition to the features provided by wx.AppConsole it keeps track of the top window (see SetTopWindow) and adds support for video modes (see SetVideoMode()).

In general, application-wide settings for GUI-only apps are accessible from wx.App (or from wx.SystemSettings or wx.SystemOptions classes).