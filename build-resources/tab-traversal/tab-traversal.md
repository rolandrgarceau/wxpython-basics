# [wx.Notebook](http://www.blog.pythonlibrary.org/2019/06/05/getting-the-correct-notebook-tab-across-platforms-in-wxpython/) how to get the right tab

This pertains to the using wx.Notebook and how to:

1. Catch the tab change event, and then...
2. Get the right tab.

Due diligence is working out as much as you can then seeking help when you know you can get the solution you are working for quicker by doing so.

### Sum up their article

The simple_note.py call to `GetCurrentPage()` was not working on all platforms- Mac being the one that seemed to be printing a one off kind of situation. In my actual testing it collects the page name
```py
current_page = self.notebook.GetCurrentPage()
print(current_page.name)
```
and confirms this tab event to be so on my MBP. Investigate further: is it really just getting the tab label text from the button, or what? There's a lot more going on here too, like themes, background colour, and performance hits with updates.