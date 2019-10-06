# [Renderer Native](https://wxpython.org/Phoenix/docs/html/wx.RendererNative.html#wx-renderernative)

* wxWidgets uses the underlying low level GUI system to draw all the controls.
* Native appearance is different under different platforms 
* renderers work by exposing a large set of high-level drawing functions which are used by the generic controls.
* There is a default global renderer but it may be changed or extended by the user, see Render Sample.

## If you override you disable things

wx.RendererNative uses "renderers" which the RendererNative is a class that virtualizes the drawing to abstract the drawing operations for you. We can use this to draw our own custom objects like buttons that may emulate the native control implementation.

There is a default global renderer but it may be changed or extended by the user, see Render Sample.

## What happens when you write your own

* Functionality may seem to "break"
* responsibility falls on the individual application

## Drawing functions take some standard parameters:

parameter | description
|---|---|
win | The window being drawn, and is normally not used.
dc | wx.DC to draw on-  Only this device context should be used for drawing.
rect | Bounding rectangle for the element to be drawn
flags | optional flags (none by default) which can be a combination of the CONTROL_FLAGS.

## Bigger concept here

Note that each drawing function restores the wx.DC attributes if it changes them, so it is safe to assume that the same pen, brush and colours that were active before the call to this function are still in effect after it.

## Subclass [wx.DelegateRendererNative](https://wxpython.org/Phoenix/docs/html/wx.DelegateRendererNative.html#wx-delegaterenderernative)

wx.DelegateRendererNative allows reuse of renderers code by forwarding all the wx.RendererNative methods to the given object and thus allowing you to only modify some of its methods without having to reimplement all of them.

Note that the “normal”, inheritance-based approach, doesn’t work with the renderers as it is impossible to derive from a class unknown at compile-time and the renderer is only chosen at run-time. So suppose that you want to only add something to the drawing of the tree control buttons but leave all the other methods unchanged.

Except for the constructor, it has exactly the same methods as wx.RendererNative and their implementation is trivial: they are simply forwarded to the real renderer. Note that the “real” renderer may, in turn, be a wx.DelegateRendererNative as well and that there may be arbitrarily many levels like this.

## Ways to make changes

* `ChangeLookAndFeel` is a call we may make here.
* Mac platform uses the system-default button color