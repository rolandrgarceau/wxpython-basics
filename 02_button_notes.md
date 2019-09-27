# [wx.Button](https://wxpython.org/Phoenix/docs/html/wx.Button.html)
```py
__init__ (self, parent, id=ID_ANY, label=””, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ButtonNameStr)
```
Constructor, creating and showing a button.

## Font Color may be dictated by Native Widgets
The button may show the font in white, depending what OS you are on. The SetForegroundColour and SetBackgroundColour (for [radio buttons](https://stackoverflow.com/questions/30901128/changing-font-color-of-wxpython-radio-button)) methods are not guaranteed to work. The reason is that 
wxPython uses the native widgets for the OS it is running on. 

#### Thought process that does not work, but it was a fair assesment based of schooling:)
The SetLabel may need to be called to populate the actual Gui display with the value it was created with as an argument passed to the constructor. My label= text might have been too long and it filled with ----- inside the actual button to test that may reflect that it couldn't fit.

### Docs on how to create buttons

The preferred way to create standard buttons is to use default value of label. If no label is supplied and id is one of standard IDs from this list, a standard label will be used. In other words, if you use a predefined ID_XXX constant, just omit the label completely rather than specifying it. In particular, help buttons (the ones with id of ID_HELP ) under OS X can’t display any label at all and while wx.Button will detect if the standard “Help” label is used and ignore it, using any other label will prevent the button from correctly appearing as a help button and so should be avoided.

In addition to that, the button will be decorated with stock icons under GTK+ 2.

Using a predefined ID_XXX constant sounds like we are defining our own selectors here for dom traversal, or a means to call out specific labels when we start talking about multiple buttons, but we need to be clear what it is we seek to obtain here. Just a font color change? Can we declare a wxStaticText object and set the foreground color and be done with it? or do we wish this for all buttons as a default?

## More support with designing [Custom Controls](https://wiki.wxpython.org/CreatingCustomControls)