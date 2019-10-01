# File Selectors
No matter what we do we need a file to work with somewhere, somehow- for both the user, the programmer, and from the promgram's perspective on a device and OS of where to look for this at.

## [wx.LoadFileSelector(what, extension, default_name="", parent=None)](https://wxpython.org/Phoenix/docs/html/wx.functions.html#wx.LoadFileSelector)
Shows a file dialog asking the user for a file name for opening a file.

## [wx.FileSelector](https://wxpython.org/Phoenix/docs/html/wx.functions.html#wx.FileSelector) Cross platform 
In Windows this is the common file selector dialog. X is called the file selector box. Path and filename are distinct elements. We can ge4t this with a dictionary and enumerate or deconstruct with path- not sure the module off the top right now.

* If path is empty, the current directory will be used.
* If filename is empty, no default filename will be supplied. 
* use wildcard to filter what is displayed as file formats displayed in the file selector.
* file extension supplies a type extension for the required filename.
* both Unix and windows support wildcard filter

Flags may be a combination of wx.FD_OPEN, wx.FD_SAVE, wx.FD_OVERWRITE_PROMPT or wx.FD_FILE_MUST_EXIST.

### Bigger Concept Here

 wx.FD_MULTIPLE can only be used with wx.FileDialog and not here since this function only returns a single file name. For this file selector we are getting at opening one file at a time. Do this first and move on. The application must check for an empty return value (the user pressed Cancel). For example:
```py
filename = wx.FileSelector("Choose a file to open")

if filename.strip():
    # work with the file
    print filename

# else: cancelled by user
```