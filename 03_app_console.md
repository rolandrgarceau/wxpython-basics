# [wx.AppConsole](https://wxpython.org/Phoenix/docs/html/wx.AppConsole.html#wx.AppConsole.OnInit)
This may be a possible way to create a hybrid "headless" mode application on a bus running in the background. Writing console-only or hybrid apps without having to define USE_GUI=0 is also an option. The functionality here will:

* set and get application-wide properties (see wx.AppConsole.CreateTraits and AppConsole.SetXXX functions)
* implement the windowing system message or event loop: events in fact are supported even in console-mode applications (see wx.AppConsole.HandleEvent and wx.AppConsole.ProcessPendingEvents );
* initiate application processing via wx.App.OnInit ;
* allow default processing of events not handled by other objects in the application (see wx.AppConsole.FilterEvent )
* implement Apple-specific event handlers (see AppConsole.MacXXX functions)

#### Bigger concept here wtih wx.AppConsole
We use the macro IMPLEMENT_APP in our application implementation file to tell wxWidgets how to create an instance of your application class.

Use DECLARE_APP in a header file if you want the wx.GetApp function (which returns a reference to your application object) to be visible to other files.

Try it yourself and see what you may accomplish here.