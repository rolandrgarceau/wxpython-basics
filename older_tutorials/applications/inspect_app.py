import wx
import wx.lib.mixins.inspection

# The default hot-key when you use the inspection tool mixin like this is Ctrl-Alt-I, or Cmd-Alt-I on Mac, but that can be changed by passing non-default parameters to the Init method. The default position and size can also be changed.

# https://wiki.wxpython.org/Widget%20Inspection%20Tool

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