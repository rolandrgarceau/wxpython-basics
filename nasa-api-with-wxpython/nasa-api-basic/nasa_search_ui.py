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
        label = wx.StaticText(self, label=txt)
        main_sizer.Add(label, 0, wx.ALL, 5)
        self.search = wx.SearchCtrl(
            self, style=wx.TE_PROCESS_ENTER, size=(-1, 25))
        self.search.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_search)
        self.search.Bind(wx.EVT_TEXT_ENTER, self.on_search)
        main_sizer.Add(self.search, 0, wx.EXPAND)

        self.search_results_olv = ObjectListView(
        self, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.search_results_olv.SetEmptyListMsg("No Results Found")
        self.search_results_olv.Bind(wx.EVT_LIST_ITEM_SELECTED,
                                    self.on_selection)
        main_sizer.Add(self.search_results_olv, 1, wx.EXPAND)
        self.update_search_results()