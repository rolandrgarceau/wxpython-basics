# contextlib.supress()

* Function available in Python 3.4 +
* selectively ignore specific exceptions using a context manager and the "with" statement:
 
```py
import contextlib

with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')

# This is equivalent to the following try/except clause:
 
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass
```