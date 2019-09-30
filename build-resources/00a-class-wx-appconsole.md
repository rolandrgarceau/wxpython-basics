# [wx.AppConsole](https://wxpython.org/Phoenix/docs/html/wx.AppConsole.html#wx.AppConsole.OnInit)
This class is essential for writing console-only or hybrid apps without having to define USE_GUI=0.

This may be a possible way to create a hybrid "headless" mode application on a bus running in the "background". Our use case here for an ROV is *NOT* exactly the way it is defined here. The functionality here with wx.AppConsole will:

* set and get application-wide properties (see wx.AppConsole.CreateTraits and AppConsole.SetXXX functions)
* implement the windowing system message or event loop: events in fact are supported even in console-mode applications (see wx.AppConsole.HandleEvent and wx.AppConsole.ProcessPendingEvents );
* initiate application processing via wx.App.OnInit ;
* allow default processing of events not handled by other objects in the application (see wx.AppConsole.FilterEvent )
* implement Apple-specific event handlers (see AppConsole.MacXXX functions)

For a offshoot process here we are talking about a variant execution of the application that can be "interjected" at will in real time by a process ID or endpoint "intervention". That is more than a hundred more pages of reading we have laid out for later.

#### Bigger concept here wtih wx.AppConsole
We use the macro IMPLEMENT_APP in our application implementation file to tell wxWidgets how to create an instance of your application class.

Use DECLARE_APP in a header file if you want the wx.GetApp function (which returns a reference to your application object) to be visible to other files.

Try it yourself and see what you may accomplish here.

## [FilterEvent](https://wxpython.org/Phoenix/docs/html/wx.AppConsole.html#wx.AppConsole.FilterEvent)

Overridden wx.EventFilter method.

This function is called before processing any event and allows the application to preempt the processing of some events, see wx.EventFilter documentation for more information.

wx.App implementation of this method always return -1 indicating that the event should be processed normally.