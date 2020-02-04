# WebView SetPage(self, *args, **kw)

The above definition is overloaded- see django-portfolio notes on args and kwargs. There is order here to be mindful of. 

With SetPage (self, html, baseUrl) using WEBVIEW_BACKEND_IE we must allow the current page to finish loading first, then we may call SetPage. I'm not sure exactly what the statement- The baseUrl is not used- is referring to in the docs.

## Request (probably in another language)

I have a html text, there is <script> tag in it, and the script need load some out source.

if I save it as a xxx.htm, and use LoadURL(file:///xxxx.htm), we can get the result.
but if I use SetPage, I get a blank page.

I saw the SetPage has 2 parameter, the second one is url, what should I give?
does the SetPage method run the js as LoadURL?

SetPage() allows you to provide the HTML you want to be displayed as a 
string, or wx.InputStream.  The second parameter is for providing a base 
URL for resolving relative links.  See documentation link for SetPage() above.

You probably just want to use LoadURL, but if you wanted to use SetPage(), 
you could load your page into a string and then pass that to SetPage().

### Google groups on the differences [here](https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!msg/wxpython-users/ZQboy9UivnQ/ZCCkfQ3DEQAJ)