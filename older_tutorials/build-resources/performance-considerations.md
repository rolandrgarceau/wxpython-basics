# Performance

Gui's entail overhead by nature. Headless means we can't necessarily see them- depending how they are coded. Python itself is designed with a single threaded interpreter, even though some people like to monkey around with that. If you need speed in real time, maybe Rust is for you, or C if that's what you know. My intent is to take this to the next level with gRPC's and see how much code can be generated this way into binaries and start performance testing containerized deployments before I can accurately report what optimizations may be in store here. 

However, some basic functionalities are worth starting a maybe list here. Maybe list the ones we know might have or entail performance hits as we encounter them, note it, and move on to fulfilling the initial requirements then come back to alternative courses of action.  

## wx.Notebook

wx.NB_NOPAGETHEME may be a windows only option that can affect performance. Supressing the "theme" may be the way to prevent performance loss.