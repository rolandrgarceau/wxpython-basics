# TextCtrl

In Mac there is font color issues with Mojave 10.14.6.

## [StyledTextCtrl](https://wiki.wxpython.org/wxStyledTextCtrl)

Is C++ wx.stc.StyleTextCtrl. https://docs.wxpython.org/wx.stc.StyledTextCtrl.html#wx-stc-styledtextctrl

Scintilla is the base component used by [wxStyledTextCtrl](https://wiki.wxpython.org/StyledTextCtrl) which gives us syntax coloring in wxPython.

## stdout or stderr to TextCtrl

For a Windows machine this approach may prove useful if one is wondering where stdout actually goes. stderr is essentially the same thing.

1. Import sys and create a TextCtrl. 
2. Set sys.stdout equal to the TextCtrl. The output will go to the TextCtrl.
3. When you are done with the window, set sys.stdout back (the wiki syntax seems to make it impossible to write double underscores outside of code blocks, see the end of the code below for how to set sys.stdout back).

```py
import wx
import sys, time

class LogWindow(wx.TextCtrl):
    def __init__ (self):
        frame = wx.Frame(None,-1, "Standard out", size=(200,200))
        frame.Show(True)

        self.parent = frame

        wx.TextCtrl.__init__(self,self.parent,size=self.parent.GetClientSize(), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)

        sys.stdout = self

        print "this is in Stdout!!!!"
        for i in range(10):
            print i
            wx.Yield()
            time.sleep(1)

        print "All done!"

class MainApp(wx.App):
    def OnInit(self):
        log = LogWindow()
        log.parent.Show(True)
        self.SetTopWindow(log.parent)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()
    sys.stdout = sys.__stdout__

```

Test: the user may encounter an exception if a secondary thread attempts to print.