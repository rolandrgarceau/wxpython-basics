# I/O Core [Heirarchy](https://github.com/python/cpython/blob/master/Lib/io.py)

* io module is where the built in open function is defined.

Class | Functionality | note
|---|---|---|
Top Abstract Class IOBase | Defines basic interface to a stream. | no separation of reading and writing to streams and OSError implementations may be raised here.
RawIOBase extends IOBase | simple reading and writing of raw bytes to a stream | FileIO subclasses this to provide interface to OS files.
BufferedIOBase | buffering on a raw byte stream from RawIOBase | subclasses BufferedWriter, BufferedReader, and BufferedRWPair buffer streams that are readable, writable, and both respectively
BufferedRandom provides a buffered interface | to random access streams | whats the random and interface?
BytesIO | simple stream of in-memory bytes | nothing is as simple as "they" say...
TextIOBase is another IOBase subclass | encodes and decodes streams into text | TextIOWrapper extends it
TextIOWrapper extends TextIOBase | is a buffered text
interface to a buffered raw stream (`BufferedIOBase`) | that even sounds raw
StringIO | in memory stream for text | which of these chickens can cross the road the fastest?

## For DEFAULT_BUFFER_SIZE
An int containing the default buffer size used by the module's buffered
I/O classes. open() uses the file's blksize (as obtained by os.stat) if
possible.