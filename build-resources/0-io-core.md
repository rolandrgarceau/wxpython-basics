# [Core I/O](https://docs.python.org/3/library/io.html#module-io)

Source from Lib/io.py. Usually hello worlds have similar basic mentality: Outline the install and then write some "stuff" to the console to know the minimums are working. This outline is a little higher up on the food chain as the "read-it-first-guide" for understanding how the application *will best* use your data as it is passed around in "la-la-land" to wherever it needs to go. Get ready for the $10 concepts tied together here after months of squirrel chasing (I'm still figuring it out as we go too btw).

## Three types of file objects defined in the [io]() module
* text i/o
* binary i/o
* raw i/o

## Concrete object is called a file object (finally hit me like a brick)

Other similar refernces are "Stream" and file-like object, independent of the category the concrete Stream object is *another* independent concrete object The file object exposes the file-oriented API with the familiar read() and write() methods *to an underlying resource*

Depending on how it was created it may get immediate access to the real file on disk, or another type of communication device or storage. This also may look like stdin character duplication if you have played with sockets and written across terminal with telnet back in the day, you may have seen those duplicate characters when transmitting/writing- thats because they also get copied to sdtout. The file like objects are streams.

In-memory text streams are also available as [StringIO](https://docs.python.org/3/library/io.html#io.StringIO) objects in Python:

```py
f = io.StringIO("some initial text data")
```

## Class [io.BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO)
Buffered I/O streams provide a higher-level interface to an I/O device than raw I/O does. A simple read from a file is one way. io.BytesIO may have been the gotcha snag for me to start exploring Python outside Lambda Functions and AWS Training. The buffer gets discarded when the close method is called. read1(\[size\]) is like read(\[size\]) here.

* stream implementation using an in-memory bytes buffer.
* inherits from BufferedIOBase. 

