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
    y = (x.title , '*' ,  x.url , '*' ,  x.top_image, '*' ,  str(x.publish_date) , '*' ,  
    replace(str(x.text.encode())), '*' ,  str(x.authors) , '*' ,  replace(str(x.summary.encode())), '*' ,  x.title, '`')
    return y
            
if __name__ == "__main__":
    search = News('nonprofit-coding-bootcamps')
    article_list = search.art_list
    columns = ['Title',	'URL', 'Image',	'Date',	'Long Description',	'Reporter Name',
           'Short Description',	'News (Title)']
    
    b = list(map(lambda each: y(each), article_list))
    with open('news.txt', 'a') as file:
        for each in b:
            file.writelines(each)