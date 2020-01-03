# [WxPython](https://wiki.wxpython.org/Getting%20Started) and Containerized deployment Tutorial Series
This repo is an attempt to learn more about wxpython and how it may work as a tool to build diagnostic Guis, and even potentially headless ones with a "flick of a switch" on embedded devices (don't call .Show(), for instance). When people talk about GUIs, they usually speak of windows, menus and icons. A wx.Window is the base class from which all visual elements are derived (buttons, menus, etc) and what we normally think of as a program window is a wx.Frame, and the view as the wx.Panel. This is an unfortunate inconsistency that has led to much confusion for new users. This repo is not just the basics, and if you are looking for that click the blue link above and follow that one instead.

## Rapid Prototyping

I am starting with the basic parts needed to create an application using wxpython for quick application development, and growing this eventually to a binary within a container to run from. This guide started with the familiarity of a few GUI frameworks, targeting wxPython in particular with the intent of accelerating further the quick deploy mentality with a tool like [PySimpleGui](https://pysimplegui.readthedocs.io/en/latest/) (see the end of the readme for the quick rundown) when sufficient understanding of the inter-workings are complete and we have a means to reference the underlying structures to build our own custom implementations of all the widgets involved. For the mean time the interpreter and build being used by wxpython install with wxpython.app will be the the first focus- the same is as the documentation outlines to install into your environment for testing with conda. We will get to the pip feeeze > requirement.txt when that time comes. For now let's move forward to the basic hello world steps.

From the basic hello world, we will design a boilerplate to build apps off of and to add functionality to, one step at a time. After getting a few applications built under our belt with adding a little bit of complexity to each sequential build, we will pause and look at how these applications may find themselves wrapped into a gRPC like generator function, assimilated into a modern microservices based binary that we can perform service discovery with, and then added to an image and eventually run as a container anywhere. Again, let us draw back to the baby steps first.

That's a tall task, and is not for the faint of heart. It takes years of dedication to your education outside of traditional channels to know how every step in this process transpires. I still do not have all those answers memorized to be able to regurgitate it in any test like fashion. But I'm getting there daily- and am learning to be more effective in documentation and repeatability surrounding the steps to success. This is a trial and error repo. My goal is to try making a few apps and document each direction taken in reading the docs, writing a little code, testing, debugging, playing back the tutorial, and repeating the processed as needed (and in any order suited to gain results) until a good personal workflow is established with these tools. The key is that it gets pen to paper and we are all actively practicing writing Python, and maybe a little C++ when wxWidgets gets put in the mix.

Maybe this repo is not for you and you need a basic tutorial on just getting wxpython to launch on your dev machine. RealPython showed me the ropes and there is countless people that can guide you down an alternate intro to building Guis than the [docs](https://wiki.wxpython.org/Getting%20Started). I am attempting to tie together concepts here in a repeatable fashion on a few platforms and with a few environment considerations with some more advanced sets of hello worlds than what may be spent searching the web to find. Hands on. In the traces.  

This will outline a means to start making 50 apps a day to be a productive software development company. I'm not trying to have a software development company just yet, and for now let's just agree to make one app at a time and see where that goes. We need POC here.

## From an Expert

I have been well informed that they start with the data model first, then the Gui. I concur. However, we as scientists that wish to fulfill a customer's wants with a product, usually are writing notes down first, then translating them into arguments, parameters, functions, methods, and eventually data-sets of potentially known columnar formats that work well with a server/client architecture. 

Starting from an in-memory dummy load of a mocked up csv file is one way to begin the process in code for a spreadsheet like entry and retrieval mechanism. Build the fake .txt file and read it into a program. Then write or draw it to a screen somehow. We might explore matplotlib with this to plot the results over time. We may even step up the text file and go for some backend architecture like Flask, but that may come after the basics are nailed. 

With time of the essence we attempt to do more contextually and have a few irons going on the fire to make it to that short sprint deadline we are attempting to match the MIT style report analysis and review with the next funding allocation to our bank account. Hopefully delegation is part of the change management plan and relinquishing control is of key value to remaining within a niche or hat to wear in that startup position. I on the other hand realize that this is the tying it all together step that may take time and patience, which will happen however long my learning curve dictates- hopefully not by the time my youngest is out of highschool. I have been patiently thinking about how to help save coral reefs for 3 decades now, and the opportunity to do so now I will not pass up.

Fast prototyping means having some of these equations running in parallel. One being the known usable application framework that is running a stable and repeatable basic program on your development machine (or prototype's embedded device). This means the program has to compile and execute on a particular device too, after you get it working on your development machine. Some may have the production and development machine in one, and that may lessen the testing if it does not need to be portable. However, we wish to use platform agnostic tooling to build with quickly and figure out a way to deploy that to a particular device so that we may fulfill the requirements coming from the customer in the first place, and then make sure the tooling will be good to be used down the road for future applications.

That said move to having the boilerplate code working with nothing but the hello world. This will allow the basic functionality of the Gui framework to be used rapidly for other cases. Turning to the actual changeable code for development we then make sure we have repeatable results in the IDE text editor, environments associated with that, and then move on to the OS we are developing with. Beware of VSCode and its terminal with conda environments as $PATH may not be what you may think it is. Know your .bash* file and what gets activated on launch, and what symlinks get followed, especially if you are building applications with different versions of dependencies within the application itself here. One may see the error: use framework download and have to deal with that- we will address this momentarily.

Think about the process of building on top of each application a little more functionality. For example one customer for an aquarium maintenance program requested a simple app to log sample results of water quality to be viewed weekly, monthly, and quarterly. If we take the idea of data entry from the perspective of water chemistry to begin one UI view (called a panel within a frame in wxpython) which we may also potentially relate to as a tabbed window view in a browser, for instance. See the section on changing views under Panel below with a wx.Notebook widget.

I will say tab for now as most can relate to a browser tab. Another tab (wx.Panel may have what we might intuitive think wx.Window might if coming from some HTML/CSS background) be could be handling water flow rates, mathematics behind them, and how to calculate staging within another panel "view" in our application. Often is the case that a customers ideas change as the project unfolds, so proper documentation is in order to be clear of what each party enters agreements into. This means when we get to our 5th or 6th sequentially more difficult application the progress might be that we have added in several layout views from our design notes and fleshed out workable frames for each (more on frames and panels in a moment) to use the grid view of column headings for importing a csv with to switch the data model around sufficiently to use numpy arrays that accomplish the grid population with, one transform at a time.

### Table Of Contents

#### Total Dissolved Solids (TDS.py)
An application to get salt water tanks reading zero to hero in no time. Grow coral. Save the planet.

#### Building Easy and Effective Documentation
If our website is solely a wiki-like informational service then we need to make searching through documentation seamless. From the Home directory any and every Class should be clickable, not just listed as there and available. In fact if we employ something like [draw.io](https://about.draw.io/use-draw-io-diagrams-in-google-docs/) for say, defining a user viewable class hierarchy map, we may do so having each member clickable and rearrangeable for interactive node display. A summary of all the Classes also mean that each has its own link. Some really good resources are out there in this fashion.   

### Basic Parts with Application
From an any application view we can start by saying there will usually be a user interface, some glue to connect it to services on the simplest of terms a file structure for persistance or a database for a backend to work with, and a means to manipulate and deal with these interactions of the user and system over time. If we are designing diagnostic systems this MVC like model may be headless, which wxpython supports a great deal of option here with. As we become familiar with their offereings and begin working our use cases, we may notice a divergence of what we consider headless and what a gui crossover program from their model might look like. 

#### Overview to Building with wxPython modules
Remember the effect of wx.Window as the building blocks and Frames as the traditional "window view". wxPython applications do not have a main procedure, but instead have a close [wx.Console.Oninit](https://wxpython.org/Phoenix/docs/html/wx.AppConsole.html#wx.AppConsole.OnInit) member defined for a class derived from the wx.App class.

All have [classes](https://wxpython.org/Phoenix/docs/html/wx.1moduleindex.html) with Capital 'C'. We write the lower case 'l' version in our code as a place holder or "variable" and in Python it's an object. `app=wx.App(already written class, we send this to "their" code, to make a class object)`. In reality it looks like 3 basic parts:

* The App
* The Frame
* The Panel

And has a few other required actions to `.show()` the parts in a window and wait for the user to do things `.mainloop()`

#### Oninit 
Is a function that we will use within the App class to perform our preparation of the application to be loaded for the OS to make use of. There are a few specific procedures to adhere to so that we do not have conflicts when performing the display of information of our application and things like updates to it.

### The [wx.App](https://wxpython.org/Phoenix/docs/html/wx.App.html#wx-app)

Applications get represented with this class. The main portions of this class to the following:

* bootstrap the wxPython system and initialize the underlying gui toolkit
* set and get application-wide properties
* implement the native windowing system main message or event loop, and to dispatch events to window instances etc.

#### Mandatory requirements of wx.App and entire program written int wxpython

wx.App also has a few primary functionalities which every app has to have: 
* A single App instance (just one declaration of this class)
* All UI objects come *after* this is class object is created.
  * This allows wxWidgets to be fully initialized

#### Normal application coding procedure

We do not have to derive a frame from this class, but it is good OOP. We may also want to deal with sizers if there is more than one frame. This can be thought of similarly like HTML flexbox or sizing based on percentages to maximize space based off total window size currently employed at the top level. More on that later. Everything can be built in the wx.App class, but best practice is to derive objects from this class that implement the OnInit(), where that Oninit() creates the *frame(s)* and then calls `self.SetTopWindow(frame)`. We may be using a derivative .Show() (check current docs for the proper call today) to perform some functionality that draws or paints to the screen for the user to see. See [app_console](wxpython-basics/03_app_console.md) for headless mode or hybrid build.

`app=wx.App(clearSigInt=True)` Clear SIGINT? This allows the app to terminate upon a Ctrl-C in the console like other GUI apps will. You should override `OnInit` to do application initialization to ensure that the system, toolkit and wxWidgets are fully initialized.

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

A book control allows users to switch between panels in a frame. wx.BookCtrlBase is the Parent Class for Book classes to inherit from. A wx.Notebook widget will present a "tabbed" control.

#### Switcheing between panels
To jump between views take a look at the tab-traversal notes section which employs the following:
* wx.Notebook(parent, id, pos, size, style)

### Gotchas

You have to use .show() to see anything. To have to add the frames and panels packed within to the main App class, and there has to be a way to init the App class and get into the main loop from the if __name__ statement.

#### Don't forget to override called out methods

How do we find out which ones have to be overidden? Some methods have to be overridden per docs- like OnInit() for the frame. This will allow your code to offer differences that the modules provided for you to use do not have. This can be found in other languages like java and even in React (the latter functionality is debateable with how it "implements"
that). 

#### We are using Python, not Java or otherwise

What is different in Python is the keyword "self". We call self.OnInit() in similar ways to other languages "this". For python projects here "self" keeps the scope, or blinders of what the other programmed code around it can see, narrowed, focused, or specific to- in this case- the class in which it is being used. As we grow complexity we will see that scope can also have an "hierarchy" of how it looks at things, and if you do a few simple prints or use the debugger to view watches, we can see the scope changing how the information is grouped and saved. More on that subject later.  

#### More [Custom Controls](https://wiki.wxpython.org/CreatingCustomControls) options and [wx.lib]()

Create custom drawn controls (wx version of css) with the code examples for using your own images.

wx.lib is a directory in the wxPython installation tree which contains a large number of "owner-drawn" widgets.

## [PySimpleGui](https://pysimplegui.readthedocs.io/en/latest/)

Just a few lines of code is all it takes to use the power of this Gui framework. However, from their documentation it appears the port with PySimpleGui is geared to TKinter, with a few others in beta ,development, and experimental. This allows someone that read down here this far an option to join a community and assist others with their findings. The cookbook and readme can be found at ReadTheDocs

### wxPython Specific readme

There exists specific documentation for using wxPython with PySimpleGui 

### The primary learning paths for PySimpleGUI are:

* [This](http://www.PySimpleGUI.org) has 100+ pages of the PySimpleGUI User Manual.
* [Cookbook](http://Cookbook.PySimpleGUI.org) with recipes to get you going and quick.
* [Demo Programs](http://www.PySimpleGUI.com) that already work
* YouTube videos
  * 5 part series of [basics](https://www.youtube.com/playlist?list=PLl8dD0doyrvHMoJGTdMtgLuHymaqJVjzt)
  * 10 part series of [more detail](https://www.youtube.com/playlist?list=PLl8dD0doyrvGyXjORNvirTIZxKopJr8s0)