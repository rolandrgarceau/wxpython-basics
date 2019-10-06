# [AdvancedSplash](https://wiki.wxpython.org/Splash%20screen%20while%20loading%20%28Phoenix%29)

Startup of wxPython that take significant time to load is tricky. The Oninit() function may experience issues if calling the [CallAfter](https://wiki.wxpython.org/CallAfter) function.

wx.CallAfter takes a function and its arguments, and calls the function when the current event handler has exited. It is a safe way of requesting action of a Window from another thread. The code below has a couple of examples.

The example app-init-call-after.py will demonstrate issues with threading and CallAfter. 

When "Click me" is pressed, onRun is called. It immediately prints "Clicky!" and issues three calls to wx.CallAfter, then waits for you to enter some text via stdin, prints the text, and returns. At this point, all pending events have been dealt with, and the commands given to CallAfter are executed. Note that the dialogs appear in reverse order.

When "Click me too" is pressed, onRun2 is called. It spawns a thread and returns. The thread executes __run, which calls CallAfter, waits for you to enter some text, prints it, and returns. In this case, however, the dialog now appears before you enter the text. This is because the event handler has already exited; the dialog was created from a thread. You can type at the prompt or close the dialog, whichever you prefer. You can even close the dialog and click on a button again before typing.

If CallAfter is not used in this second circumstance, crashes occur. Change

wx.CallAfter(self.AfterRun, "I appear immediately (event handler\n"+ \
                        "exited when OnRun2 finished)")
to

self.AfterRun("I appear immediately (event handler\n"+ \
                        "exited when OnRun2 finished)")
Run the program and click on "Click me too". Dismiss the dialog box and click either button again (before typing anything) to witness the event dispatch thread becoming very confused.

