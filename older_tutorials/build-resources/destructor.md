# Wxpython destructor

## Using the __del__ method

It is invoked automatically when the instance (object) of the class is about to get destroyed. We can use it to clean up resources like closing a file. This normally happens when the class is about to finish and is no longer needed. We need to be more explicit of the functionality surrounding the wxPython destructor, however, to become good at understanding what is done for us, and what we do not have responsibility cleaning up. 

A notable here is things like garbage collection and how far a good program or *programmer* has to go to achieve a "clean slate". With Python unused objects such as built-in types or instances of the classes are automatically deleted (removed) from memory when they are no longer in use. Are we having to override a particular `def __del__:` or does this happen with default behavior? More specifically do we need to call out such things here as any preclose features before the child windows close?