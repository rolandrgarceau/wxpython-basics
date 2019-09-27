# WxPython
There should be a few examples to get started in here. We will be starting with the basic parts of an application using wxpython and growing this eventually to a binary within a container to run from. From the basic hello world we will design a boilerplate to build apps off of and to add functionality to, one step at a time. After getting a few applications built under our belt with a little bit of complexity, we will pause and look at how this application finds itself wrapped into a gRPC like generator function, assimilated into a modern microservices based binary, and then added to an image and eventually run as a container anywhere. 

That's a tall task, and is not for the faint of heart. It takes years of dedication to your education outside of traditional channels to know how every step in this process transpires, (I still do not have all those answers and am learning more about them every day) so do not get frustrated if there is holes in your understanding. Maybe this repo is not for you and you need a basic tutorial on just wxpython. RealPython showed me the ropes and there is countless people that can guide you down the intro to building Guis.   

This will outline a means to start making 50 apps a day to be a productive software development company. I'm not trying to have a software development company, and for now let's just agree to make one at a time and see where that goes.

## From an Expert

I have been informed that they start with the data model first, then the Gui. I concur. However we as scientists that wish to fulfill a customer's wants with a product usually are writing notes down first, then translating them into arguments, parameters, functions, methods, and eventually data-sets of known columnar formats that work well with a server/client architecture. Starting from an in memory dummy load of a mocked up csv file is one way to begin that process in code. Build the fake .txt file and read it into a program. Then write or draw it to a screen. With time of the essence we attempt to do more contextually and have a few irons going on the fire to make it to that short sprint deadline we are attempting to match the MIT style report analysis and review with the next funding allocation to your bank account. Hopefully delegation is part of your change management plan and relinquishing control is of key value to remaining within your niche or hat to wear in your startup position.

Fast prototyping means having these equations running in parallel. One being the known usable application framework that is running a stable and repeatable basic program on your development machine (or prototype's embedded device). This means the program has to compile and execute on a particular device. However, we wish to use platform agnostic tooling to build with quickly and figure out a way to deploy that to a particular device so that we may fulfill the requirements coming from the customer in the first place.

That said move to having the boiler working with nothing but the hello world. Then make sure we have repeatable results in the IDE text editor, environments associated with that, and then move on to the OS we are developing with. Beware of VSCode and its terminal with conda environments as $PATH may not be what you may think it is. Know your .bash* file and what gets activated on launch, and what symlinks get followed, especially if you are building applications with different versions here. One may see the use framework download and have to deal with that- the answer is coming momentarily.

Think about the process of building on top of each application a little more functionality. For example if we take the idea of data entry from the perspective of water chemistry to begin one panel view in our application, this means when we get to our 5th or 6th sequentially more difficult application the progress might be to use the grid view of column headings for importing a csv with to swith the data model around sufficiently to use numpy arrays that accomplish the grid population with, one transform at a time.

### Table Of Contents

#### Total Dissolved Solids (TDS.py)
An application to get salt water tanks reading zero to hero in no time.

## Building Easy and Effective Documentation
If our website is soly a wiki-like informational service then we need to make searching through documentation seamless. From the Home directory any and every Class should be clickable, not just listed as there and available. A summary of all the Classes also mean that each has its own link.

### Basic Parts of this kinda Application
All have [classes](https://wxpython.org/Phoenix/docs/html/wx.1moduleindex.html) with Capital 'C'. We write the lower case 'l' version in our code as a place holder or "variable" and in Python it's an object. `app=wx.App(already written class, we send this to "their" code, to make a class object)`. In reality it looks like 3 basic parts:

* The App
* The Frame
* The Panel

ANd has a few other required actions to `.show()` the parts in a window and wait for the user to do things `.mainloop()`

### The [App](https://wxpython.org/Phoenix/docs/html/wx.App.html#wx-app)
`app=wx.App(clearSigInt=True)` Clear SIGINT? This allows the app to terminate upon a Ctrl-C in the console like other GUI apps will.  You should override `OnInit` to do application initialization to ensure that the system, toolkit and wxWidgets are fully initialized.

### The [Frame](https://wxpython.org/Phoenix/docs/html/wx.Frame.html#wx.Frame)
Contains Appearance, Events, Styles, and Frame Emitters

#### Appearance
The main "window" a user sees. There are a few preselected options here for CSS-like appearance:

* wxMSW
* wxGTK
* wxMAC

#### Events
There are a few `Default` events the Frame processes:

* wxEVT_SIZE- will exclude the status and toolbar and take the entire frame client area if there is only one child window, and if we use more than one we need to use sizers.
* wxEVT_MENU_HIGHLIGHT:

#### Styles
Window styles default to normal, resizable frames. There are extra styles.

#### Frame Emitters
Event Macros. We may program a `wx.Window.Close`. There may be a `CLOSE_BOX` style for the upper right x option if available, and we can even look at [wx.CloseEvent](https://wxpython.org/Phoenix/docs/html/wx.CloseEvent.html#wx-closeevent) for more info.

An application should normally define an wx.CloseEvent handler for the frame to respond to system close events, for example so that related data and subwindows can be cleaned up.

### The [Panel](https://wxpython.org/Phoenix/docs/html/wx.Panel.html?highlight=panel)
The portion that contains the widgets, buttons, etc, need to be added to the frame. A panel is a window on which controls are placed. There are Emitters with handlers here as well. The main feature over its parent class `wx.Window` is code for handling child windows and TAB traversal, which is implemented natively if possible (e.g. in wxGTK) or by wxWidgets itself otherwise.

### Gotchas

You have to use .show() to see anything. To have to add the frames and panels packed within to the main App class, and there has to be a way to init the App class and get into the main loop from the if __name__ statement.

#### Dont forget to override called out methods

How do we find out which ones have to be overidden? Some methods have to be overridden per docs- like OnInit() for the frame. This will allow your code to offer differences that the modules provided for you to use do not have. This can be found in other languages like java and even in React (the latter functionality is debateable with how it "implements"
that). 

#### We are using Python, not Java or otherwise

What is different in Python is the keyword "self". We call self.OnInit() in similar ways to other languages "this". For python projects here "self" keeps the scope, or blinders of what the other programmed code around it can see, narrowed, focused, or specific to- in this case- the class in which it is being used. As we grow complexity we will see that scope can also have an "hierarchy" of how it looks at things, and if you do a few simple prints or use the debugger to view watches, we can see the scope changing how the information is grouped and saved. More on that subject later.  

#### More [Custom Controls](https://wiki.wxpython.org/CreatingCustomControls) options and [wx.lib]()

Create custom drawn controls (our version of css) with the code examples for using your own images.

wx.lib is a directory in the wxPython installation tree which contains a large number of "owner-drawn" widgets.