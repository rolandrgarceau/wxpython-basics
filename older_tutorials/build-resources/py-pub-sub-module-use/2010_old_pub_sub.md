# [OLD EXAMPLE](http://www.blog.pythonlibrary.org/2010/06/27/wxpython-and-pubsub-a-simple-tutorial/)! Use this for reference *ONLY*

An old example from 2010, they used `pubsub` module which was originally accessed from wx.lib.pubsub. Back then it was available from sourceforge to download as a standalone, but was actually included in wxpython. The alternate then was also PyDispatcher, which django.dispatch and their "signals" came from.

This example uses the built-in version to communicate between two frames, and with one being possibly hidden. Sometimes we need to open a non-modal frame to get information from a user, and then pass that information back to the application’s main frame. Additionally a simple use we may want to employ is just to tell one frame the other closed (look at modern panel implementations using `self` today for this).

This current example addresses both of the above communication issues. We may find actual implementation usage for our series of tutorials more similar to [tutorialspoint](https://www.tutorialspoint.com/wxpython/wx_dialog_class.htm) instead of this older pub sub example, but understanding the evolution may help increase the lower wheel reinventing process. We may employ a file dialog box instead at first instantiation of an application to select a particular working file to add to, and its implementation details quite a bit different than the details here, so just keep that in mind. 

Understanding non-modal frames  (may be also referred to as modeless) may warrant understanding such implications of this design pattern as it relates to user input and frame acknowledgement of the users selection being communicated to another portion of the application. Specifically this knowledge may needed to modify headless diagnostics if communications might happen across a network or between containers, or may be used for other caching mechanisms not yet divulged upon. 

For me, labeling classes with "other" frame and "main" frame is confusing enough, especially when still trying to differentiate what a "frame" is as it pertains to wxPython. Some may argue that we may be skipping steps here, but for those that need a visual representation of classes in action, it may be beneficial to rename these classes to something you are actually using- like say a motor safety class that is checking amperage of a pump and the values of current being discovered by your breakout board class or something. Try not to be distracted by words. For me that translates to more than just labels in code.  

```py
import wx
from wx.lib.pubsub import Publisher
 
########################################################################
class OtherFrame(wx.Frame):
    """uses the show.mainframe to call the showFrame method for pub sub"""
 
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
        msg = self.msgTxt.GetValue() # just text from the text controls value
        Publisher().sendMessage(("show.mainframe"), msg) # here we send to the "subscribed"
        #this hits the MainFrame
        self.Close()
 
 
########################################################################
class MainPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
 
        Publisher().subscribe(self.showFrame, ("show.mainframe")) # this is the "subscribe" with topic name "mainframe"
 
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

Notice below the "subscribe" line with topic name "mainframe" from within the MainPanel class
```py
Publisher().subscribe(self.showFrame, ("show.mainframe")) 
```
Other parts of the program can publish to that topic and the listener will pick them up and call the “showFrame” method. Refer to the “OtherFrame” class “onSendAndClose” method describing this in code.

```py
# this code is above in the OtherFrame class

def onSendAndClose(self, event):
    """
    Send a message and close frame
    """
    msg = self.msgTxt.GetValue() # simple example here only uses the text control's text value
    # we may in reality be getting a value from a db or a computation somewhere in another tab
    # e.g. an aquarium application may need the pump cfm and current values to periodically check safety system
    Publisher().sendMessage(("show.mainframe"), msg)
    self.Close()
```

To send it from the OtherFrame Class, we call the Publisher object’s sendMessage method and pass it the topic string and the message. The message can be a list of objects or just a single object. In this case, it’s just a string. Back in the MainPanel, the showFrame method gets called. 

So from the MainPanel class we see the `def showFrame(self, msg):` method.

```py
# From the MainPanel class above
def showFrame(self, msg):
    """
    Shows the frame and shows the message sent in the
    text control
    """
    self.pubsubText.SetValue(msg.data) # pubsub data property
    frame = self.GetParent() # there may be a hidden frame somewhere
    frame.Show() 
```

In this method we extract the data sent through pubsub via its `data` property. If we had sent multiple items using a list, we’d need to do something like msg.data[0] to get at the right item (assuming the string was in element one). 

## Newer API for latest `pubsub`

There is slightly different API functionality today. There could still be some trouble creating a binary with the newest pubsub using a slightly older API like the one from sourceforge, the original post of this article was using wxPython around version 2.8.11.0. A [Google Groups thread](https://groups.google.com/forum/#!topic/wxpython-users/1EikKr2uPmk) for details from 2010 is still available describing inconsistencies with py2exe and some possible alternatives, just be aware these may not hold at all relevant today.

The entire example above shows the basics to communicate between two frames with one hidden. It also shows how to pass information from one frame to the other. We will expand on this knowledge when looking at file dialog boxes and possibly use this as the means to get information from our user in the first step, and then pass the result on to the application to work with after that.

