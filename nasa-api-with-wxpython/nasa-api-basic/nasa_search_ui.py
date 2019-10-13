# nasa_search_ui.py
 
import os
import requests
import wx
 
from download_dialog import DownloadDialog
from ObjectListView import ObjectListView, ColumnDefn
from urllib.parse import urlencode, quote_plus

class Result:
 
    def __init__(self, item):
        data = item['data'][0]
        self.title = data['title']
        self.location = data.get('location', '')
        self.nasa_id = data['nasa_id']
        self.description = data['description']
        self.photographer = data.get('photographer', '')
        self.date_created = data['date_created']
        self.item = item
 
        if item.get('links'):
            try:
                self.thumbnail = item['links'][0]['href']
            except:
                self.thumbnail = ''

class MainPanel(wx.Panel):
 
    def __init__(self, parent):
        super().__init__(parent)
        self.search_results = []
        self.max_size = 300
        self.paths = wx.StandardPaths.Get()
        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
 
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        txt = 'Search for images on NASA'
        label = wx.StaticText(self, label=txt)#header label for the application
        main_sizer.Add(label, 0, wx.ALL, 5)
        # SearchCtrl is like TextCtrl with built in buttons
        self.search = wx.SearchCtrl(
            self, style=wx.TE_PROCESS_ENTER, size=(-1, 25))
        # we bind BOTH of the following to a click event handler on_search
        self.search.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_search)
        self.search.Bind(wx.EVT_TEXT_ENTER, self.on_search)
        main_sizer.Add(self.search, 0, wx.EXPAND)

        # add the search results widge
        self.search_results_olv = ObjectListView(
        self, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.search_results_olv.SetEmptyListMsg("No Results Found")
        self.search_results_olv.Bind(wx.EVT_LIST_ITEM_SELECTED,
                                    self.on_selection)
        main_sizer.Add(self.search_results_olv, 1, wx.EXPAND)
        self.update_search_results()

        #add a title text control and an image widget that will update when a result is selected

        main_sizer.AddSpacer(30)
        self.title = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.title.SetFont(font)
        main_sizer.Add(self.title, 0, wx.ALL|wx.EXPAND, 5)
        img = wx.Image(240, 240)
        self.image_ctrl = wx.StaticBitmap(self,
                                        bitmap=wx.Bitmap(img))
        main_sizer.Add(self.image_ctrl, 0, wx.CENTER|wx.ALL, 5
                    )
        download_btn = wx.Button(self, label='Download Image')
        download_btn.Bind(wx.EVT_BUTTON, self.on_download)
        main_sizer.Add(download_btn, 0, wx.ALL|wx.CENTER, 5)
        
        self.SetSizer(main_sizer)

    # also add a download button to allow the user to select which image size they would like to download

    def on_download(self, event):
    selection = self.search_results_olv.GetSelectedObject() #get the user’s selection
    if selection:
        with DownloadDialog(selection) as dlg:
            dlg.ShowModal()

    def on_search(self, event):
        search_term = event.GetString()
        if search_term:
            query = {'q': search_term, 'media_type': 'image'}
            full_url = base_url + '?' + urlencode(query, quote_via=quote_plus)
            r = requests.get(full_url)
            data = r.json()
            self.search_results = []
            for item in data['collection']['items']:
                if item.get('data') and len(item.get('data')) > 0:
                    data = item['data'][0]
                    if data['title'].strip() == '':
                        # Skip results with blank titles
                        continue
                    result = Result(item)
                    self.search_results.append(result)
            self.update_search_results()
    def on_selection(self, event):
        selection = self.search_results_olv.GetSelectedObject()
        self.title.SetValue(f'{selection.title}')
        if selection.thumbnail:
            self.update_image(selection.thumbnail)
        else:
            img = wx.Image(240, 240)
            self.image_ctrl.SetBitmap(wx.Bitmap(img))
            self.Refresh()
            self.Layout()