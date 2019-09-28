# wx.AppTraits

* The wx.AppTraits class defines various configurable aspects of a wx.App.
* AppTraits is an abstract class since it contains many pure virtual functions

## Acsess to them

* wx.App.GetTraits function
* Create your own wx.AppTraits overriding the wx.App.CreateTraits function.

### Connect a few objects here

By default, wxWidgets creates a ConsoleAppTraits object for console applications (i.e. those applications linked against Base library only - see the page) and a GUIAppTraits object for GUI applications. Both these classes are derived by wx.AppTraits and represent concrete implementation of the wx.AppTraits interface.

