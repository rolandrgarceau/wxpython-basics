import wx

# just to show the basics, then we will wipe this clean and put in proper classes
# this won't work unless your environment is proper though
the_app = wx.App(clearSigInt=True)
the_frame = wx.Frame(parent=None , id=wx.ID_ANY, title='01_app', pos=(100,100))
# id is the window id, the first one he didnt care about
# pos position to launch on desktop
the_panel = wx.Panel(parent=the_frame, id=wx.ID_ANY)
#notice the lower 'f'
welcome_text=wx.StaticText(parent=the_panel, id=wx.ID_ANY, label="dude wheres my ROV?") # no pos
# ownership is the panel- thats where it will reside- wxPython has widgets we will see later 

# We still have to display it to the screen
the_frame.Show()
# and finally wait around for something to happe
the_app.MainLoop()

