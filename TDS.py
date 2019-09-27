import wx

class TheApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        #init the frame
        self.InitFrame()
    def InitFrame(self):
        #frame = wx.Frame(parent, id=ID_ANY, title=EmptyString, pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameSt)
        frame = TheFrame(parent = None, title = "Total Dissolved Solids report", pos = (100,100))
        frame.Show(True)

class TheFrame(wx.Frame):
    # subclass of wx.Window; Frame is a top level window
    # A frame is a window whose size and position can be changed by the user, or fixed/locked down.
    # Usually represents the first/main window a user will see
    def __init__(self, parent, title, pos): 
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()
    # from docs calls out to override OnInit
    def OnInit(self):
        panel = ThePanel(parent=self)
        #panel.Show()

class ThePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # add in the starter boilerplate text
        # welcome = wx.StaticText(parent, id=ID_ANY, label=EmptyString, pos=DefaultPosition, size=DefaultSize, style=0, name=StaticTextNameStr)
        welcomeText = wx.StaticText(self, id=wx.ID_ANY, label="Boiler Starts Here", pos=(20,20))

if __name__ == "__main__":
    app = TheApp()
    app.MainLoop()
