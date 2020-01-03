# [wx.Log](https://wxpython.org/Phoenix/docs/html/wx.Log.html#wx-log)

Defines the interface for the log targets used by wxWidgets logging functions as explained in the Logging Overview. There are already derived default log targets with standard implementations of it for you, but this class can help make your own personal versions. 

That said if we decide to use the standard default we should only have to worry about wx.LogDebug, wx.LogError, wx.LogMessage and similar functionsm, which have the same syntax as the standard Python [logging module](https://docs.python.org/3/library/logging.html)

## Use module-level functions here, not instantiated classes directly

We always want to use functions to derive info instead of direct instantiation. E.g. calling `logging.getLogger(name)`. Multiple calls to getLogger() with the same `name` will always return a reference to the same Logger object. The name is potentially a period-separated hierarchical value, like wegot.the.log but could just be a single thelog with no periods. The period after the first wegot (.) means that eveything after the period are decendants of the wegot logger. This child like addendum policy can help ingesting traces or figuring out where the originating log came from. 

## From wx.AppTraits

Can we create an async function using HasStderr() which will sit and await a potential error condition? From documentation :

[HasStderr()](https://wxpython.org/Phoenix/docs/html/wx.AppTraits.html#wx-apptraits)
Returns True if fprintf(stderr) goes somewhere, False otherwise.