# [wx.Notebook](Thttps://wxpython.org/Phoenix/docs/html/wx.Notebook.html)

This class represents a notebook control, which manages multiple windows with associated tabs.

NotebookPage is a typedef for wx.Window.

## Styles
Are where the tabs appear on the screen in the app. Wxpython referred to them as Window Styles. This class supports the following styles:

wx.NB_TOP: Place tabs on the top side.
wx.NB_LEFT: Place tabs on the left side.
wx.NB_RIGHT: Place tabs on the right side.
wx.NB_BOTTOM: Place tabs under instead of above the notebook pages.
wx.NB_FIXEDWIDTH: (Windows only) All tabs will have same width.
wx.NB_MULTILINE: (Windows only) There can be several rows of tabs.
wx.NB_NOPAGETHEME: (Windows only) Display a solid colour on notebook pages, and not a gradient, which can reduce performance.
The styles wx.NB_LEFT, wx.RIGHT and wx.BOTTOM are not supported under Microsoft Windows when using visual themes.

## Emitters

Handlers bound for the following event types will receive a wx.BookCtrlEvent parameter.

EVT_NOTEBOOK_PAGE_CHANGED: The page selection was changed. Processes a wxEVT_NOTEBOOK_PAGE_CHANGED event.
EVT_NOTEBOOK_PAGE_CHANGING: The page selection is about to be changed. Processes a wxEVT_NOTEBOOK_PAGE_CHANGING event. This event can be vetoed.

## default theme paints a background on the notebook’s pages.

We may choose to supress this behavior, and there is three ways to do so:

1. NB_NOPAGETHEME can disable themed drawing for a particular notebook
2. call wx.SystemOptions.SetOption to disable it for the whole application
3. disable it for individual pages by using `SetBackgroundColour` which will disable themed pages globally: