# [Core I/O](https://docs.python.org/3/library/io.html#module-io)

Source from [Lib/io.py](https://github.com/python/cpython/blob/master/Lib/io.py). Read the github readme on the base I/O heirarchy in Python first (IOBase is an abstract class). Usually hello worlds have similar basic mentality: Outline the install and then write some "stuff" to the console to know the minimums are working. This outline is a little higher up on the food chain as the "read-it-first-guide" for understanding how the application *will best* use your data as it is passed around in "la-la-land"- to wherever it needs to go. Get ready for the $10 concepts tied together here after months of squirrel chasing (I'm still figuring it out as we go too, btw). 

## Three types of file objects defined in the [io]() module
* text i/o
* binary i/o
* raw i/o

## Concrete object is called a file object (finally hit me like a brick)

Other similar references are terms used like "Stream" and file-like object. Independent of the category the concrete Stream object is *another* independent concrete object The file object exposes the file-oriented API with the familiar read() and write() methods *to an underlying resource*. Which ones, you say?

Depending on how it was created it may get immediate access to the real file on disk, or another type of communication device or storage. This also may look like stdin character duplication if you have played with sockets and written across a terminal with telnet, you may have seen those duplicate characters when transmitting/writing- thats because they also get copied to stdout. The file like objects are streams.

In-memory text streams are also available as [StringIO](https://docs.python.org/3/library/io.html#io.StringIO) objects in Python:

```py
f = io.StringIO("some initial text data")
```

## Class [io.BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO)

Buffered I/O streams provide a higher-level interface to an I/O device than raw I/O does. A simple read from a file is one way. io.BytesIO may have been the gotcha snag for me to start exploring Python outside Lambda Functions and AWS Training. Cutting and pasting just doesn't do it for the average computer scientist (or does it?). The buffer gets discarded when the close method is called. read1(\[size\]) is like read(\[size\]) here.

* stream implementation using an in-memory bytes buffer.
* inherits from BufferedIOBase. 

### Step away from the madness for a minute if it hurts:)

This is complicated concepts, with an attempted not-so-complex delivery. Go get a coffee, take a week to digest it, whatever you need to process this long term. For me, it has been 2 or so years of hitting it a few times here and there with maybe less than what some may consider "optimal" results (especially if your deadline is a 2 week sprint). However, memory management is the jest of this paragraph, so get it right now and feel good that you are providing optimal results later when you are seeing traces and can't tell if its due to insomnia, or just a bad configuration file:) 

# Stream IO *IS NOT* StringIO

If you scan read things too fast, these two words may be interpreted for the same, yet again ambiguous terms we may have seen in many, many documentation sites and frameworks. I missed this the first time around, and this now has been a revelation for me. Reconfigure your mind- I had to hit reboot a few times for it to kick in:

```py
import io

# from docs
output = io.StringIO()
output.write('First line.\n')
print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close() # or test a with statement and see if you get the is closed = true... 

```

Hopefully your mental reboot is awaiting stdin input questions like:

* What's the max buff size?
* Can we blow it out here? 

### getvalue() out of getting hit with a metaphoric brick:)

From the class io.StringIO, this function will give you an *entire* string representation of the buffer. Newlines are decoded as if by [read()](https://docs.python.org/3/library/io.html#io.TextIOBase.read), although the stream position is not changed. Don't get this right and your program might hit you with that brick, for real. Following the rabbit hole to [TextIOBase](https://docs.python.org/3/library/io.html#io.TextIOBase.read) and the above read() we see this explanation:

### read(size=-1)
Read and return at most size characters from the stream as a single str. If size is negative or None, reads until EOF. Can we answer a few questions above here, or are we still searching for ENV_VARS such as MAX_WELL_HOUSE_CAFE? Take a glance at the `readline(size=-1)` right below the read() description:

### readline(size=-1)
Read until newline or EOF and return a single str. If the stream is already at EOF, an empty string is returned.

If size is specified, at most size characters will be read.

### Go for it

Connecting this with code:
```py
# see file-open.py
```
