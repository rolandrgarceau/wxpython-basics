# wxPython and 2020 Clarity 

Explore more after getting your conda environment activated with python 3.8 ish and wxPython Pheonix at least 4.04. Current today's writing is 4.0.7. Watch trying to follow the classic migration guide (thise pre 4.0 are considered classic) for fisrt time- just follow the steps below with conda if using a Mac. If supporting other developer's applications this may be useful knowledge coming in from behind a team to add features or fix broken functionality. Main wiki [here](https://wiki.wxpython.org)

## Install Guide [here](https://wiki.wxpython.org/How%20to%20install%20wxPython)

Follow instructions for MacOS. I'm not backing any other platform instal here, but will answer questions on most Linux distros if the question is well formed.

### [Downloads](https://www.wxpython.org/pages/downloads/)

Use pip to build from the released source archives, or from the source archives created in the pre-release snapshot builds. I use conda and recommend offloading some install responsibilities that way.

### [Github](https://github.com/wxWidgets/Phoenix)

Binaries available at PyPI can be confusing to build yourself, even with a CS degree. Be careful using the build.py commands- that's all I have to say about that. It does come with unit tests, however.

Github version will help build wxPython from a workspace checked out from the wxPython Phoenix repository if using your own custom version, else follow conda or conda-forge below, or the downloads to pip above.

I have been using conda for environment orchestration. Conda and conda-forge are not the same leading install versions, so be aware of the caveats to each. 

The notes on pythonw are outdated and may no longer be necessary. I have been executing apps with the normal python call since the older_tutorials directory with wxPython.

### WxPython API [official docs](https://docs.wxpython.org)

Get the offline API and user manual called wxPython-docs-VERSION.tar.gz

### Support Groups

When AA just isn't cutting it, try [wxpython-dev google group](https://groups.google.com/forum/#!forum/wxpython-dev)

### Other wxPython based [applications](https://wiki.wxpython.org/wxPythonPit%20Apps)