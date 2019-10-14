## Debugging Techniques

Unhandled exceptions are considered bugs. The program will abort with a traceback for finding where this ocurred. The traceback is routed to stdio, captured in a GUI Frame independent from your application. If an exception shows up in an event handler, the traceback is displayed, and hopefully your program will keep working (wxPython allows non-fatal execution to continue, obviously).

Initialization errors, however, will allow the traceback to show up then your program aborts. this forces the stdio window with your traceback to close faster than you can see what happened. You can keep stdio from being hijacked by wxPython by providing a couple of optional parameters when you instantiate your wxApp. Try this from the [docs](https://wiki.wxpython.org/Getting%20Started):

```py
class MyApp (wx.App):
#...
#...
#...
myapp = MyApp() # functions normally. Stdio is redirected to its own window
myapp = MyApp(0) #does not redirect stdout. Tracebacks will show up at the console.
myapp = MyApp(1, 'filespec') #redirects stdout to the file 'filespec'
# NOTE: These are named parameters, so you can do this for improved readability:
myapp = MyApp(redirect = 1, filename = 'filespec') # will redirect stdout to 'filespec'
myapp = MyApp(redirect = 0) #stdio will stay at the console...
```

## wxPython Widget Inspection [Tool](https://wiki.wxpython.org/Widget%20Inspection%20Tool)

In just two lines we can add this option into the application directly, or we can add a class with a hot-key stroke to activate our code with. Debug in IDE's can be tricky, require more configuration, and distract a developer from the actual code in front of them. VSCode has watches we can define, but try this to see a predrawn debug window:

```py
import wx.lib.inspection
wx.lib.inspection.InspectionTool().Show()
```

### Same tool as its own built-in with hot key

```py 

import wx
import wx.lib.mixins.inspection

class MyFrame(wx.Frame):
    pass
 
class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    def OnInit(self):
        self.Init()  # initialize the inspection tool
        frame = MyFrame(None, title="This is a test")
        frame.Show()
        self.SetTopWindow(frame)
        return True

app = MyApp()
app.MainLoop()

```
### Parts of the tool have their own documentation

PyFilling is a Python namespace viewer, part of the Py collection of programs. The Py Manual has documentation for PyAlaCarte, PyAlaMode, PyCrust, PyFilling, PyShell, and PyWrap:

http://www.orbtech.com/www/PyManual.html
http://www.wxpython.org/PyManual.html

* PyCrust is an interactive Python shell that displays at the bottom of the tool.
  * 
* PyAlaMode is a Python code editor
* PyAlaCarte is a Python code editor
* PyWrap is a runtime utility that lets you run an existing wxPython program with a PyCrust frame at the same time. Inside the PyCrust shell namespace, the local variable app is assigned to your application instance. In this way you can introspect your entire application within the PyCrust shell, as well as the PyFilling namespace viewer. And through the use of the Py decorator classes, PyCrust can display wxPython function and method signatures as well as docstrings for the entire wxPython library.