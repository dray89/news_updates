# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:24:39 2019

@author: rayde
"""

from news_sources import ticker_df, articles
'''
create data frame of stock tickers
'''
tickers = ticker_df(entertainment)
stocks = tickers.get_df()
links = tickers.run_search(stocks)

'''
create articles from search, uses search from previous function to build articles
'''
a = articles()
a.build_articles(links)