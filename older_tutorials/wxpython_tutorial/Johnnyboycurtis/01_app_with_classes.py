import wx

class TheApp(wx.App):
    ''' The wx.App class represents the application and is used to:
    * bootstrap the wxPython system and initialize the underlying gui toolkit
    * set and get application-wide properties
    * implement the native windowing system main message or event loop, and to dispatch events to window instances etc.
    '''
    def __init__(self):
        # How do we wish to close the app through the terminal?
        super().__init__(clearSigInt=True)

        # init the frame so it can be used in the application
        self.InitFrame()
    def InitFrame(self):
        ''' to be called by TheApp class after initialization to create the frame, 
        subclass of wx.Frame: Creating the frame with our class will allow the app to "draw" it with a .Show()
        @param parent: whom up the food chain does this feed?
        @param title: displays on the top task bar
        @param pos: where it needs to be launched on the device's screen (think grid)
        '''
        #
        # Default initialization will happen with the following if not specified in our program:
        #
        # frame = TheFrame(parent, id=ID_ANY, title=EmptyString, pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameSt)
        frame = TheFrame(parent = None, title = "Total Dissolved Solids report", pos = (300,300))
        frame.Show(True)# without this it may run in the background with nothing to see

class TheFrame(wx.Frame):
    '''
    subclass of wx.Window; Frame is a top level window
    A frame is a window whose size and position can (usually) be changed by the user.
    Usually represents the first/main window a user will see
    '''
    def __init__(self, parent, title, pos): # call out default pos?
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()
    # from docs calls out to override OnInit
    def OnInit(self):
        panel = ThePanel(parent=self)

class ThePanel(wx.Panel):
    ''' Class usually added to the frame to add functionality with. 
    Primarily used for handling child windows and TAB traversal, which is implemented natively if possible (e.g. in wxGTK) or by wxWidgets itself otherwise.
    Parent Class wx.Window
    '''
    def __init__(self, parent):
        super().__init__(parent=parent)

        # add in the starter boilerplate text
        # default values for Static method if not called out during object initialization
        #
        # welcome = wx.StaticText(parent, id=ID_ANY, label=EmptyString, pos=DefaultPosition, size=DefaultSize, style=0, name=StaticTextNameStr)
        welcome = wx.StaticText(self, id=wx.ID_ANY, label="Boiler Starts Here", pos=(100,100))

if __name__ == "__main__":
    app = TheApp()
    app.MainLoop()
