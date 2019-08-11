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

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from newspaper import Article, nlp

class NewsSearch:
    def __init__(self, searchterm):
        self.searchterm = searchterm
        self.texts = []
        self.links = []
        self.date = []
        self.art = []
        self.GoogleSearch()
    
    def GoogleSearch(self):
        self.url="https://news.google.com/rss/search?q=" + self.searchterm + "&hl=en-US&gl=US&ceid=US%3Aen"
        Client=urlopen(self.url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        # Print news title, url and publish date
        for news in news_list:
          self.texts.append(news.title.text)
          self.links.append(news.link.text)
          self.date.append(news.pubDate.text)
          
        for link in self.links:
            self.article = Article(link)
            try:
                self.article.build()
                self.article.nlp()
            except:
                pass
            finally:
                self.art.append(self.article)
                