# [Django Signals](https://github.com/django/django/tree/master/django/dispatch) 

[django.dispatch](https://github.com/django/django/tree/master/django/dispatch) is Django Signals and was based off PyDispacher. django.dispatch may offer more limited interface, but higher performance; requires that signals be objects of a given type, and eliminates `Any` registrations. Registrations are on the signal objects.

## [PyDispatcher](https://code.launchpad.net/pydispatcher)

PyDispatcher authored by Mike Fletcher is available as a standard Python `distutils` installation package from the Python Package Index (PyPI) with no binaries, so we may not have dependency issues. The above link is to launchpad, however. Version 2.0.5 offers Python 3.x support via shared code-base (not 2to3). Python 2.x is still the primary development target, however.

Handler functions in PyDispatcher are relatively loose in their definition. A handler can simply declare the parameters it would like to receive and receive only those parameters when the signal is sent.  The sender can include extra parameters for those handlers which require them without worrying about whether a more generic handler can accept them:

def handle_specific_event( sender, moo ):
    """Handle a simple event, requiring a "moo" parameter"""
    print 'Specialized event for %(sender)s moo=%(moo)r'%locals()
dispatcher.connect( handle_specific_event, signal=SIGNAL2, sender=dispatcher.Any )

## OpenGLContext based off PyDispatcher

OpenGLContext uses PyDispatcher to provide a link between PyVRML97 (model level) and OpenGLContext (the controller and view levels).

## PyQt specific Software 

Louie is based off PyDispatcher too. 