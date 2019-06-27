
import csv
from matplotlib import pyplot as plt

search_Sentences = ['장자연','버닝썬']
Date = []
JJY_News = []
BN_News = []
for search_Sentence in search_Sentences:
    
    file_Name = search_Sentence + '_Naver'
    
    file_Directory = 'Data/Naver/'+file_Name 
    
    file = open(file_Directory+'.csv','r', encoding='euc-kr',newline='')
    
    csvReader = csv.reader(file)
    
    
    for line in csvReader:
        
        if line[0] == '검색어':
            Date += []
        
        
        
        else: 
            if search_Sentence == '장자연':
            
                Date.append(line[1])

                JJY_News.append(int(line[2]))
        
            
            if search_Sentence == '버닝썬':
           
                BN_News.append(int(line[2]))
            
            

plt.figure(figsize=(30, 3))          
plt.plot(Date, JJY_News, 'r-', label="The number of news about 'Jang Ja Yeon'")
plt.plot(Date, BN_News, 'g-', label="The number of news about 'Burning Sun'")

plt.legend(loc=2)

plt.title("The trend of news about 'Jang Ja Yeon' and 'Burning Sun'(2019.01.10~2019.05.27)")
plt.xlabel('Date')
plt.ylabel('The number of news')
plt.show()

for search_Sentence in search_Sentences:
    file_Name = search_Sentence
    file_Directory = 'Data/Naver' + file_Name
    file.close()