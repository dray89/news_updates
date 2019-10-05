# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:54:17 2019

@author: rayde
"""

import newspaper
from newspaper import Article, fulltext
from GoogleNews import GoogleNews
import pandas as pd
import traceback
from news_updates.news_sources import News

def textfile(self, document_name, index_list):
    with open(document_name, 'w+') as doc:
        for each in list(index_list):
            doc.write(each+'\n')