# [PyPubSub](https://dzone.com/articles/tutorial-on-wxpython-4-and-pubsub)

Deprecated, but already built in wxPython GUI from years ago in `wx.lib.pubsub`. The implementation is based on the `PyPubSub` package. We could download the package and use it directly without any additional dependency. There is an old .py file that here shows slight modification to the import for creating this functionality with a modern use case.

There is also an old package we may not use from 2015 called [PyDispatcher](https://pypi.org/project/PyDispatcher/) which was the Multi-producer-multi-consumer signal dispatching mechanism. This helped with event routing with various application contexts. Included in the PyDispatcher package were the `robustapply` and `saferef` modules, which gave us the ability to selectively apply arguments to callable objects and to reference instance methods using weak-references. A derivative of the project provides the Django web framework's "signal" system. PyDispatcher is maintained on the LaunchPad project in bzr by Mike Fletcher.

