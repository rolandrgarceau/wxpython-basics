# wxPython Dialog [tutorial](https://www.tutorialspoint.com/wxpython/wx_dialog_class.htm) 

From the top level Dialog is for user interaction with the application. Even though the Dialog class object may appear like a Frame, it is usually used as a pop-up window on top of a parent frame. We use a `Dialog` to collect data from the user and send it to the parent frame. A `Dialog` frame can be modal (where it blocks the parent frame) or modeless where the dialog frame can be actually bypassed. See the common methods section for implementation details and how values get passed around in this context. `ShowModal()` method displays dialog frame in the modal manner, while `Show()` makes it modeless. See my tutorial example for more description on this topic.

Pre-configured `Dialog` widgets in wxPython are available: 

* MessageDialog
* FileDialog
* FontDialog
* more...

wx.Dialog supports the use of Sizers just like a wx.Frame object does. Because of this a custom Dialog can be designed.

## Wx.Dialog class constructor (BIG 'W'?)

```py
wx.Dialog(parent, id, title, pos, size, style)
```

## Common methods

Method | Description
|---|---|
DoOK() | Called when OK button on the dialog is pressed
ShowModal() | Shows the dialog in application modal fashion
ShowWindowModal() | Dialog is modal to top level parent window only
EndModal() | Ends a modal dialog passing the value from ShowModal invocation

* The `Default` appearance of Dialog widget shows only Close box in the title bar. However, it can be customized using style parameters. 

## Pre-configured widgets

There are also pre-configured commonly used buttons for Dialog -> MessageDialog.
