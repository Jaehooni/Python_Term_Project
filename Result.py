import datetime
from News_finder import news_Finder
start = datetime.date(2019,1,5)
end = datetime.datetime.now()
search_Sentences = ['버닝썬', '장자연']
for search_Sentence in search_Sentences:
    file_Name = search_Sentences
    news_Finder(search_Sentence,start,end,file_Name)