%matplotlib inline
from matplotlib import pyplot as plt
import csv
A_News = []
B_News = []
Trend_1 = input()
Trend_2 = input()


start = datetime.date(2019,1,20)

end = datetime.date(2019,5,1)

search_Sentences = ['용산 참사','강호순 연쇄 살인 사건']

for search_Sentence in search_Sentences:
    
    file_Name = search_Sentence + '_Naver' + '(' + str(start.strftime('%Y.%m.%d')) + '~' + str(end.strftime('%Y.%m.%d')) + ')' 
    
    news_Finder(search_Sentence,start,end,file_Name)
    

    
for search_Sentence in search_Sentences:
    
    file_Name = search_Sentence + '_Naver' + '(' + str(start.strftime('%Y.%m.%d')) + '~' + str(end.strftime('%Y.%m.%d')) + ')' 
    
    file_Directory = 'Data/Naver/'+file_Name + '.csv'
    
    file = open(file_Directory,'r', encoding='euc-kr',newline='')
    
    csvReader = csv.reader(file)

    
    
    for line in csvReader:
        
    
        if line[0] != '검색어':
             
                
            if search_Sentence == '장자연':

                A_News.append(int(line[2]))
                
            
            if search_Sentence == '버닝썬':
           
                B_News.append(int(line[2]))
    
            
xs = list(range(1,len(A_News) + 1))

            
Graph_title = "The trend of news about '{}' and '{}'".format(Trend_1,Trend_2) + '(' +  start.strftime('%Y.%m.%d') + '~' + end.strftime('%Y.%m.%d') + ')' 
plt.figure(figsize=(30, 3))          
plt.plot(xs, A_News, 'r-', label="The number of news about 'Jang Ja Yeon'")
plt.plot(xs, B_News, 'g-', label="The number of news about 'Burning Sun'")

plt.legend(loc=2)



plt.title(Graph_title) 
plt.xlabel('Day_delta from start_date')
plt.ylabel('The number of news')
plt.show()

for search_Sentence in search_Sentences:
    file_Name = search_Sentence
    file_Directory = 'Data/Naver' + file_Name
    file.close()
