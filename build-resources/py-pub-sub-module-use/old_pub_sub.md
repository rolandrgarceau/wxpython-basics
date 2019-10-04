# [OLD EXAMPLE](http://www.blog.pythonlibrary.org/2010/06/27/wxpython-and-pubsub-a-simple-tutorial/)! Use this for reference *ONLY*

An old example from 2010, they used `pubsub` module which was originally accessed from wx.lib.pubsub. Back then it was available from sourceforge to download as a standalone, but was actually included in wxpython. The alternate then was also PyDispatcher, which django.dispatch and their "signals" came from.

This example uses the built-in version to communicate between two frames. Sometimes we need to open a non-modal frame to get information from a user, and then pass that information back to the application’s main frame. Additionally a simple use we may want to employ is just to tell one frame the other closed (look at modern panel implementations today for this).

This example addresses both of the above issues. We may find actual implementation usage for our series of tutorials to use a file dialog box at first instantiation of the application to select a particular working file to add to, which may warrant understanding such implications of this design pattern as it relates to user input and frame acknowledgement of the users selection being communicated to another portion of the application. Specifically this may need to happen if the communications happen across a network or between containers. 

```py
import wx
from wx.lib.pubsub import Publisher
 
########################################################################
class OtherFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY, "Secondary Frame")
        panel = wx.Panel(self)
 
        msg = "Enter a Message to send to the main frame"
        instructions = wx.StaticText(panel, label=msg)
        self.msgTxt = wx.TextCtrl(panel, value="")
        closeBtn = wx.Button(panel, label="Send and Close")
        closeBtn.Bind(wx.EVT_BUTTON, self.onSendAndClose)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        flags = wx.ALL|wx.CENTER
        sizer.Add(instructions, 0, flags, 5)
        sizer.Add(self.msgTxt, 0, flags, 5)
        sizer.Add(closeBtn, 0, flags, 5)
        panel.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def onSendAndClose(self, event):
        """
        Send a message and close frame
        """
        msg = self.msgTxt.GetValue()
        Publisher().sendMessage(("show.mainframe"), msg)
        self.Close()
 
 
########################################################################
class MainPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
 
        Publisher().subscribe(self.showFrame, ("show.mainframe"))
 
        self.pubsubText = wx.TextCtrl(self, value="")
        hideBtn = wx.Button(self, label="Hide")
        hideBtn.Bind(wx.EVT_BUTTON, self.hideFrame)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pubsubText, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(hideBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def hideFrame(self, event):
        """"""
        self.frame.Hide()
        new_frame = OtherFrame()
        new_frame.Show()
 
    #----------------------------------------------------------------------
    def showFrame(self, msg):
        """
        Shows the frame and shows the message sent in the
        text control
        """
        self.pubsubText.SetValue(msg.data)
        frame = self.GetParent()
        frame.Show()
 
########################################################################
class MainFrame(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Pubsub Tutorial")
        panel = MainPanel(self)
 
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()

```

## Explination: MainPanel class

Publisher().subscribe(self.showFrame, ("show.mainframe"))