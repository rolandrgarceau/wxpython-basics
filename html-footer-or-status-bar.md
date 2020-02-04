# Footer

## Request

A HTML "footer" where a "banner" is fixed to the bottom of the screen- much like how most newer web pages look.

Do you mean the bottom of the screen, or the bottom of your window?  The bottom of your window is easy.  Use a vertical box sizer as your outer most sizer, then add a spacer just above your banner and make it growable.  It will suck up any extra space and shove your banner to the bottom.

```py
# status bar
self.statusbar = self.CreateStatusBar()
self.statusbar.SetFieldsCount(4)
self.statusbar.SetStatusWidths([-1, -1, -1, -3])
self.statusbar.SetStatusText('Something interesting', 1)
```

This implementation may also be look upon from the bottom up. Some methods employ negative numbers to refer to the process of going from the "end" back one or three (check that the SetStatusWidths does this).