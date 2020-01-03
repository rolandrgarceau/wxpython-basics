# [PyPubSub](https://dzone.com/articles/tutorial-on-wxpython-4-and-pubsub)

See below for [2019 versions](https://github.com/schollii/pypubsub) of PyPubSub as January and March address issues for backward and by month, also slightly backward compatibility.

Deprecated, but already built in wxPython GUI from years ago in `wx.lib.pubsub` is demonstrated here with `old_pub_sub.py`. The implementation is based on the `PyPubSub` package. We could download the package and use it directly without any additional dependency. There is an old .py file that here shows slight modification to the import for creating this functionality with a modern use case called `newer_py_pub_sub.py`. 

## PyDispatcher has many, many spinoffs like Django signals to name just one popular one

There is also an old package we may not use from 2015 called [PyDispatcher](https://pypi.org/project/PyDispatcher/) which was the Multi-producer-multi-consumer signal dispatching mechanism. This helped with event routing with various application contexts. Included in the PyDispatcher package were the `robustapply` and `saferef` modules, which gave us the ability to selectively apply arguments to callable objects and to reference instance methods using weak-references. A derivative of the project provides the Django web framework's "signal" system. PyDispatcher is maintained on the LaunchPad project in bzr by Mike Fletcher. there is an included section in these noted with more information on this.

## The modifications for newer use

The main difference here between using the built-in PubSub is the import.

All you need to do is replace this if using wxPython 2.9 or greater:
```py
from wx.lib.pubsub import pub
```
with this:
```py
from pubsub import pub
```

If you were stuck using wxPython 2.8, then you will need to see how the PubSub API changed since the older version. If you are using wxPython 2.9 or greater, then it should be straight forward.

## Subscribe to a topic:
```py
pub.subscribe(self.myListener, "panelListener")
```

## And next publish to that topic:
```py
pub.sendMessage("panelListener", message=msg)
```

## More reading on wxPython versions 2.9

Still dated from [2013](https://www.blog.pythonlibrary.org/2013/09/05/wxpython-2-9-and-the-newer-pubsub-api-a-simple-tutorial/) but adds in sizers to the mix.

## Moving up through Python 3.x with [PyPubSub in 2019](https://github.com/schollii/pypubsub)

Notice January release was for above 3.x versions of Python while the March release geared all of 2.7.x

