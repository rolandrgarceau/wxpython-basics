# Event Handling

Every Gui's responsibility is to deal with events and to handle the users creation of them. Old-skul was the switch we relied upon for doing an action. With object oriented programming we have two more complex ways to deal with ways to distribute information between applications.

#### Java style event handlers

We attach these to the objects and bind them to callback functions/methods. The object receives the event handler, and the event handler triggers the function.

#### Predetermined method name assignments for handles

WE may modify how a particular class responds to a particular event. WE derive the class an then overload the method.

## wxPython Way

wxPython combines both situations above- define event handlers along with deriving classes to implement new behaviors.

#### self.Bind(wx.EVT_SOMETHING, ACallable)

The .Bind above says that when the SOMETHING event is delivered to this window (self), and it comes from any child window or itself, then call ACallable. self must be a class derived from a wxPython window (e.g. a Button, a Dialog, a Frame), and "ACallable" can be any function, normally we just make it a function within the above-mentioned class.