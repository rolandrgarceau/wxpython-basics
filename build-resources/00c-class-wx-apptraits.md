# wx.AppTraits

* The wx.AppTraits class defines various configurable aspects of a wx.App.
* AppTraits is an abstract class since it contains many pure virtual functions

## Acsess to them

* wx.App.GetTraits function
* Create your own wx.AppTraits overriding the wx.App.CreateTraits function.

### Connect a few objects here

By default, wxWidgets creates a ConsoleAppTraits object for console applications (i.e. those applications linked against Base library only - see the page) and a GUIAppTraits object for GUI applications. Both these classes are derived by wx.AppTraits and represent concrete implementation of the wx.AppTraits interface.

### Methods
CreateConfig(self)
Called by wxWidgets to create the default configuration object for the application.

The default version creates a registry-based RegConfig class under MSW and wx.FileConfig under all other platforms.

The wx.App.GetAppName and wx.App.GetVendorName methods are used to determine the registry key or file name.

Return type:	wx.ConfigBase

CreateEventLoop(self)
Used by wxWidgets to create the main event loop used by wx.App.OnRun .

The default implementation of this method in GUIAppTraits returns the usual platform-specific GUI event loop. The version in ConsoleAppTraits returns a console-specific event loop which can be used to handle timer and socket events in console programs under Unix and MSW or None under the other platforms where console event loops are not supported yet.

Return type:	wx.EventLoopBase

CreateLogTarget(self)
Creates a wx.Log class for the application to use for logging errors.

The default implementation returns a new wx.LogGui class.

Return type:	wx.Log
See also wx.Log

GetDesktopEnvironment(self)
This method returns the name of the desktop environment currently running in a Unix desktop.

Currently only “KDE” or “GNOME” are supported and the code uses the X11 session protocol vendor name to figure out, which desktop environment is running. The method returns an empty string otherwise and on all other platforms.

Return type:	string

GetStandardPaths(self)
Returns the wx.StandardPaths object for the application.

It’s normally the same for Base and GUI except in the case of Mac and Cocoa.

Return type:	wx.StandardPaths
Note The returned reference is to a StandardPathsBase class but you can consider it to be equivalent to wx.StandardPaths (which is documented).

GetToolkitVersion(self)
Returns the wxWidgets port ID used by the running program and eventually fills the given pointers with the values of the major, minor, and micro digits of the native toolkit currently used.

The version numbers returned are thus detected at run-time and not compile-time (except when this is not possible e.g. Motif).

E.g. if your program is using wxGTK port this function will return wx.PORT_GTK and put in given pointers the versions of the GTK library in use. See PlatformInfo for more details.

If a micro version is not available it will have a value of 0.

Return type:	tuple
Returns:	( wx.PortId, major, minor, micro )

HasStderr(self)
Returns True if fprintf(stderr) goes somewhere, False otherwise.

Return type:	bool

IsUsingUniversalWidgets(self)
Returns True if the library was built as wxUniversal.

Always returns False for Base-only apps.

Return type:	bool

ShowAssertDialog(self, msg)
Shows the assert dialog with the specified message in GUI mode or just prints the string to stderr in console mode.

Returns True to suppress subsequent asserts, False to continue as before.

Parameters:	msg (string) –
Return type:	bool

