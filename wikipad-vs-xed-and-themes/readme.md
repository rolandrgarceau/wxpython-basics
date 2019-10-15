# [WikidPad](https://en.wikipedia.org/wiki/WikidPad) vs Xed

* Official site for [WikidPad](http://wikidpad.sourceforge.net)

These are tools to address note taking and planning, to increase developer productivity. WikidPad was created by Jason Horman who released it under his own open source license, similar to the BSD license, in June 2005. Since October 2005 Michael Butscher has been the main developer of WikidPad. WikidPad can store notes in plain text or a SQLite database. When storing notes as text, the program can use SQLite or Gadfly to index the text files. Plug-ins can be addeed to WikidPad to aide functionality.


## Themes and presentation with wxPython 

Dealing with themes we are presented different build paths to the look and feel. I received an issue in my inbox dealing with theme topics presented within a WikidPad and Xed. Some builds begin with a default of "theme-less" settings, and we are modifying our look and feel to suit by adding in customized themes.

Conda environments may hold different dependencies, thus versioning may also be a potential area for dirrent outputted "themes". Anaconda may package a particular GTK to deal with themes too. There is not a lot of posts on the web concerning this as of mid Oct. 2019, but we may look at:

## gobject-introspection

## GTK2 vs GTK3

### Conda Forge build YAML and Further notes

From a user employing a wxpython app from wxpython installed with Anaconda on Linux Mint 19.2 Cinnamon. His build had the wxpython packaged by conda forge (4.0.6) which pulls in its own gtk2. These [docs](https://github.com/conda-forge/wxpython-feedstock/blob/master/recipe/meta.yaml) show the meta.yaml file which is used in the aformentioned build. HOWEVER, if you look closely at the [standard anaconda channel site] we can see that there is another package that deals out a different GTK with version 4.0.4, so be very aware of our channel and what we pull into our environment.

I had similar choices when looking at the channel and version to pull into my beginning projects too with wxPyhton. This may affect the look and feel, but if we are doing our part as developers, hopefully addressing the "CSS" like nature of layouts have already been dealt with by the time we get to this step, and our environment has been planned accordingly. Sadly enough, people with money want to see results, so sometimes we sprint without walking first.