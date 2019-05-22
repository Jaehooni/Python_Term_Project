import requests
import datetime
import csv
from bs4 import BeautifulSoup



def news_Finder(search_Sentence,start,end,file_Name):
    
    '''
    (str,datetime.date,datetime.date(or datetime.datetime),str) ---> str
    This function shows the number of news of particular date from start to end.
    
    '''
    
    #end에서 하루를 더 더한 날짜를 20XX.XX.XX 형태로 나타내어 반복문에서 원래 now 일자까지의 기사 개수가 나오도록 조정함.
    end += datetime.timedelta(days=1)

    #20XX.XX.XX로 형태를 조정하는 이유: naver에서 리퀘스트 할때 이 형태여야 하기 때문이다.
    end_Date = end.strftime('%Y.%m.%d')

    #기사 개수를 보길 원하는 시작 날짜을 20XX.XX.XX 형태로 나타냄.
    start_Date = start.strftime('%Y.%m.%d')
    

    while start_Date != end_Date:
        
        #어떤 날짜인지 표시
        print(start_Date)

        #네이버에 리퀘스트를 요청할 날짜를 search_Date로 설정함.
        search_Date = start_Date


        #네이버에서 특정 일자의 특정 단어가 들어간 기사의 개수를 찾기 위한 URL 양식
        address = 'https://search.naver.com/search.naver?where=news' + '&query={}&pd=3&ds={}&de={}'.format(search_Sentence,search_Date,search_Date)
        
        print(address)

        # HTTP GET Request
        req = requests.get(address)
       
        #html 소스 가져오기
        html = req.text
        
        # BeautifulSoup으로 html소스를 python객체로 변환하기
        # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.

        all_news_information = BeautifulSoup(html, 'html.parser')
        
        #Copy selecter에 의해 복사된 태그 사이에 들어가는 정보만 가져옴, 여기서는 뉴스 개수만 가져오기 위함임.
        news_number_info = all_news_information.select('#main_pack > div.news.mynews.section._prs_nws > div.section_head > div.title_desc.all_my > span')

        #엑셀 차트로 표현하기 위해서 csv 모듈 이용해서 파일 작성
        file = open('data/'+file_Name+'.csv','w', encoding='euc-kr',newline='')
        csvWriter = csv.writer(file)

        #뉴스 개수가 존재하지 않아 태그에 해당하는 정보가 존재하지 않을 때 0건이라는 내용 출력
        if not news_number_info:
            
            csvWriter.writerow([search_Sentence,search_Date,'0건'])


        #데이터들 중에서 온전히 뉴스 개수만 가져오기 위한 과정
        else:

            news_number_info = news_number_info[0]
            news_number_info = str(news_number_info)
            change_to_news_number = news_number_info.split(' / ')
            change_to_news_number = change_to_news_number[1]
            change_to_news_number_2 = change_to_news_number.split('<')
            only_news_number = change_to_news_number_2[0]

            csvWriter.writerow([search_Sentence,search_Date,only_news_number])


        # 한 과정이 끝날때마다 다음 날짜 뉴스로 넘어가기 위함
        start = start + datetime.timedelta(days=1)
        start_Date = start.strftime('%Y.%m.%d')
       