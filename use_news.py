# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:13:03 2019

@author: rayde
"""
from news_sources import News
from datetime import date

def replace(a):
    return a.replace('\\n', " ").replace('\\xe2\\x80\\x99', "'").replace("b'", '')

def y(x):
    y = (x.title, ' #womenintech #womenwhocode #datascience' ,";",  x.url, '\n')
    return y
            
if __name__ == "__main__":
    search = News('nonprofit-coding-bootcamps', 120)
    article_list = search.art_list    
    b = list(map(lambda each: y(each), article_list))
    with open('news.txt', 'a', encoding='utf-8') as file:
        for each in b:
            file.writelines(each)