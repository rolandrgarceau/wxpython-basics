# USE_GUI

The wx.App class represents the application itself when USE_GUI=1 .

## [wx.GetApp()](https://wxpython.org/Phoenix/docs/html/wx.functions.html#wx.GetApp)

Can return a wx.AppConsole type.

## Headless horseman or headless chicken?

By default, wxWidgets creates a ConsoleAppTraits object for console applications (i.e. those applications linked against Base library only - see the page) and a GUIAppTraits object for GUI applications. Both these classes are derived by wx.AppTraits and represent concrete implementation of the wx.AppTraits interface.


