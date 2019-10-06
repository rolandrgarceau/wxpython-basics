# Local Images may build from known paths

After the data model has been addressed, discussed, and sometimes not fully complete for sake of "sprint deadlines" or squirrel flashy-light sidetracks (I know we all have good excuses here for this one), we have to open files from the structure we have agreed upon. It may be in memory and lost when the program terminates, so we also may have more to do when it comes to running in memory apps then assigning a bind mount to the residing path to persistence. In larger teams and software builds this becomes more increasingly necessary to define and document well up front, but sometimes you just have to get it done to meet the deadline, nad then go back and make sense of it later when you tell the forces that press ink to your check that there is more things to be done to not have fragile codebase for release to production.

This basic step will allow us to connect a file open dialog with what is really happening in code. Sometimes the prebuilt solutions use these exact methods for us and it is not apparent at first, second, or even third glance for some us. In any event we press on to our customers deadline. Make a working application, document all the possible skipped steps we know of, ask for more money and more time, and then fix our backlogs based off a prioritization schedule.

## Script Execution usually starts from a particular $PATH 

Start with getting the correct information for where we are executing from. From anywhere to here, right now deployed on the I don't care what device for now:) Notice some maybe newer concepts here to consider- the way in which super is called which may affect your inheritance model, and the way in which we may append strings to a particular path for defining where images may reside in your program.

A good test to convince ourselves we are working from a good path is to try running a cli command `python ../different-directory/app_from_other_directory.py` after we get the images actually running in the current application. More specifically cd out of the directory you may be working in for this example notes and run the from_cwd_images.py file and see that it is in fact using the os call for the local cwd as it should and not grabbing your shell path's cwd instead.

Then a better test later may come in for the in memory usage and bind mounts that may not be on the local machine- like from a network path that has authentication tokens required to submit a request with. More on that when we deal with client/server architecture for wxPython.

## wxPython and local images

There are a few pre-built module options in wxPython to use images with. First we can use a wx.Bitmap as a base means to bring in things like *.jpg images into our program. Then we may need need to deal with resizing of the images. Another module here to consider is wx.Image and finally wx.Icon for small images. Employing each tactic in code is depending on how it is to be used, and there are specific procedures involved to get this functioning. 

### With our example program we:

1. Use the Frame to define the place from which the image will be used in our example. This means we need a path to work with. Make sure the module os grabs the correct one- we may not be getting this locally from disk in all applications.
  * When we use things like icons in the top left corner they may be specific to a taskbar or menubar per OS or device native implementations, just be aware of the inheritance issues we may be creating
2. Make a bitmap to bring the image in from the wx.Bitmap(self.path-to-image) module.
  * assign the path with the constructor
3. Set the icon to that created image
  * watch using self.here we may need to pass the bitmap to something like the wx.Icon() constructor first