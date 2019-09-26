# WxPython
There should be a few examples to get started in here. Some may be forked from github repos.

## Building Easy and Effective Documentation
From the Home directory any and every Class should be clickable, not just listed as there and available. 

### Basic Parts of this kinda Application
All have [classes](https://wxpython.org/Phoenix/docs/html/wx.1moduleindex.html) with Capital 'C'. We write the lower case 'l' version in our code as a place holder or "variable" and in Python it's an object. `app=wx.App(already written class, we send this to "their" code, to make a class object)`. In reality it looks like 3 basic parts:

* The App
* The Frame
* The Panel

ANd has a few other required actions to `.show()` the parts in a window and wait for the user to do things `.mainloop()`

### The [App](https://wxpython.org/Phoenix/docs/html/wx.App.html#wx-app)
`app=wx.App(clearSigInt=True)` Clear SIGINT? This allows the app to terminate upon a Ctrl-C in the console like other GUI apps will.  You should override `OnInit` to do application initialization to ensure that the system, toolkit and wxWidgets are fully initialized.

### The [Frame](https://wxpython.org/Phoenix/docs/html/wx.Frame.html#wx.Frame)

#### Appearance
The main "window" a user sees. There are a few preselected options here for CSS-like appearance:

* wxMSW
* wxGTK
* wxMAC

#### Events
There are a few `Default` events the Frame processes:

* wxEVT_SIZE- will exclude the status and toolbar and take the entire frame client area if there is only one child window, and if we use more than one we need to use sizers.
* wxEVT_MENU_HIGHLIGHT:

#### Styles
Window styles default to normal, resizable frames. There are extra styles.

#### Frame Emitters
Event Macros. We may program a `wx.Window.Close`. There may be a `CLOSE_BOX` style for the upper right x option if available, and we can even look at [wx.CloseEvent](https://wxpython.org/Phoenix/docs/html/wx.CloseEvent.html#wx-closeevent) for more info.

An application should normally define an wx.CloseEvent handler for the frame to respond to system close events, for example so that related data and subwindows can be cleaned up.

### The Panel
The portion that contains the widgets, buttons, etc, need to be added to the 'f'rame.

### Gotchas

You have to use .show() to see anything. To have to add the frames and panels packed within to the main App class, and there has to be a way to init the App class and get into the main loop from the if __name__ statement.