# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:51:42 2019
''' sends news updates '''
@author: rayde

"""
from newspaper import Article
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import numpy as np

class News:
    def __init__(self, searchterm):
        '''
        

        Parameters
        ----------
        searchterm : Formatted search term (no spaces allowed use -)
        number : TYPE, optional
            The number of results the search should yield. The default is 20.

        Returns
        -------
        None.

        '''
        self.term = searchterm
        self.url= "https://news.google.com/rss/search?q=" + searchterm + "&hl=en-CA&gl=CA&ceid=CA%3Aen"
        self.links = set()
        self.art_list = []
        self.GoogleSearch()
        

    def GoogleSearch(self):
        Client=urlopen(self.url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        self.news_list=soup_page.findAll("item")
    
    def links(self):
        for each in self.news_list:
            self.links.add(each.link.text)
    
    def article_list(self):
        for link in self.links:
            art = Article(link)
            try:
                art.build()
                art.nlp()
            except:
                pass
            finally:
                self.art_list.append(art)
                
    def count_words(self):
        wordcounts = np.array([len(each.text.split()) for each in self.art_list])
        return wordcounts
        
    def keywords(self):
        keywords = [each.keywords for each in self.art_list]     
        return keywords 
    
            