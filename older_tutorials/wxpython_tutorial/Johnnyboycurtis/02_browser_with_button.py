import wx
import webbrowser

class TheApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        #init the frame
        self.InitFrame()
    def InitFrame(self):
        #frame = wx.Frame(parent, id=ID_ANY, title=EmptyString, pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameSt)
        frame = TheFrame(parent = None, title = "Total Dissolved Solids report", pos = (300,300))
        frame.Show(True) # without this it may run in the background with nothing to see

class TheFrame(wx.Frame):
    # subclass of wx.Window; Frame is a top level window
    # A frame is a window whose size and position can (usually) be changed by the user.
    # Usually represents the first/main window a user will see
    def __init__(self, parent, title, pos): # call out default pos?
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()
    # from docs calls out to override OnInit
    def OnInit(self):
        panel = ThePanel(parent=self)

class ThePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # add in the starter boilerplate text
        #welcome = wx.StaticText(parent, id=ID_ANY, label=EmptyString, pos=DefaultPosition, size=DefaultSize, style=0, name=StaticTextNameStr)
        welcome = wx.StaticText(self, id=wx.ID_ANY, label="Boiler Starts Here", pos=(20,20))
        # button = wx.Button(parent, id=ID_ANY, label=EmptyString, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ButtonNameStr)
        button = wx.Button(self, label = "click", pos = (20,80)) #looks like text is white color 
        # button.Bind(event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)
        button.Bind(event=wx.EVT_BUTTON, handler=self.onSubmit)

    def onSubmit(self, event):
        # misspelled kttps://... instead of https: url lends a launch with firefox
#         0:65: execution error: An error of type -10814 has occurred. (-10814)
# 69:77: execution error: Can’t get application "chrome". (-1728)
# 2019-09-27 11:42:35.190 Python[81141:1163752] IMKClient Stall detected, *please Report* your user scenario attaching a spindump (or sysdiagnose) that captures the problem - (imkxpc_attributesForCharacterIndex:reply:) block performed very slowly (2.76 secs).
        # proper spelling launches Safari (default launch?)
        webbrowser.open('https://wxpython.org/Phoenix/docs/html/index.html')

if __name__ == "__main__":
    app = TheApp()
    app.MainLoop()
