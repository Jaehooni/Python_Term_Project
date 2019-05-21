from News_finder import news_Finder
NF.to = NF.datetime.datetime.now()
NF.from_ = NF.datetime.date(2019,1,5)
NF.search_Sentence = '버닝썬'
NF.news_Finder(NF.search_Sentence,NF.from_,NF.to)
