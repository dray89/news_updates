# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:51:42 2019
''' sends news updates '''
@author: rayde

call using:

a = ticker_df(tickerlist)
a.objects[0].title
a.objects[0].keywords
a.objects[0].summary

"""

import urllib.request   
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

class News:
    def __init__(self, searchterm):
        self.term = searchterm
        self.url= "https://news.google.com/rss/search?q=" + searchterm + "&hl=en-US&gl=US&ceid=US%3Aen"
        self.GoogleSearch()
        
    def GoogleSearch(self):
        Client=urlopen(self.url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        self.news_list=soup_page.findAll("item")
        