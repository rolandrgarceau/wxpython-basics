# [Sizers](https://wiki.wxpython.org/Getting%20Started)

A sizer (that is, one of the wx.Sizer sub-classes) can be used to handle the visual arrangement of elements within a window or frame. 

* Calculates the appropriate size for the visual element 
* Position elements according to particular rules
* Dynamic resizing happens when a frame is resized

## Common types of Sizers

Type | Description
|---|---|
wx.BoxSizer | which arranges visual elements in a line going either horizontally or vertically.
wx.GridSizer | which lays visual elements out into a grid-like structure.
wx.FlexGridSizer | which is similar to a wx.GridSizer except that it allow for more flexibility in laying out visual elements.

## Using Sizers

Sizers get a list of wx.Window objects to perform sizing on. We add objects 2 ways with sizer.Add(window, options...) or by calling sizer.AddMany(...). Sizer will only work on the objects it is given. So add them all for automatic management. 

### Nesting

Sizers can be nested. We can add one sizer to another sizer, for example to have two rows of buttons (each laid out by a horizontal wx.BoxSizer) contained within another wx.BoxSizer which places the rows of buttons one above the other. Observe how the additions occur.

## Breakdown of the sizer.py file

The sizer.Add method has three arguments. The first one specifies the control to include in the sizer. The second one is a weight factor which means that this control will be sized in proportion to other ones. For example, if you had three edit controls and you wanted them to have the proportions 3:2:1 then you would specify these factors as arguments when adding the controls. 0 means that this control or sizer will not grow. The third argument is normally wx.GROW (same as wx.EXPAND) which means the control will be resized when necessary. If you use wx.SHAPED instead, the controls aspect ratio will remain the same.

If the second parameter is 0, i.e. the control will not be resized, the third parameter may indicate if the control should be centered horizontally and/or vertically by using wx.ALIGN_CENTER_HORIZONTAL, wx.ALIGN_CENTER_VERTICAL, or wx.ALIGN_CENTER (for both) instead of wx.GROW or wx.SHAPED as that third parameter.

You can alternatively specify combinations of wx.ALIGN_LEFT, wx.ALIGN_TOP, wx.ALIGN_RIGHT, and wx.ALIGN_BOTTOM. The default behavior is equivalent to wx.ALIGN_LEFT | wx.ALIGN_TOP.
One potentially confusing aspect of the wx.Sizer and its sub-classes is the distinction between a sizer and a parent window. When you create objects to go inside a sizer, you do not make the sizer the object's parent window. A sizer is a way of laying out windows, it is not a window in itself. This has similar functionality to what the original Frames did when introduced in VB6 pre 2006 if that tells you how long I've been paying attention. About long enough the squirrel took to write that sentence:) In the above example, all six buttons would be created with the parent window being the frame or window which encloses the buttons -- not the sizer. If you try to create a visual element and pass the *sizer as the parent window*, your program will crash.

Once you have set up your visual elements and added them to a sizer (or to a nested set of sizers), the next step is to tell your frame or window to use the sizer. You do this in three steps:
```py
window.SetSizer(sizer)
window.SetAutoLayout(True)
sizer.Fit(window)
```
The SetSizer() call tells your window (or frame) which sizer to use. The call to SetAutoLayout() tells your window to use the sizer to position and size your components. And finally, the call to sizer.Fit() tells the sizer to calculate the initial size and position for all its elements. If you are using sizers, this is the normal process you would go through to set up your window or frame's contents before it is displayed for the first time.