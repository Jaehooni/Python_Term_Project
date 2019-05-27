from News_finder import news_Finder
import datetime
import requests
import csv
from bs4 import BeautifulSoup
import time

start = datetime.date(2019,1,10)
end = datetime.datetime.now()
search_Sentences = ['장자연','버닝썬']
for search_Sentence in search_Sentences:
    file_Name = search_Sentence
    news_Finder(search_Sentence,start,end,file_Name)
