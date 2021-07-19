#-*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup



url = "https://finance.naver.com/sise/sise_market_sum.nhn"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

res = requests.get(url, headers=headers)            

#print(res.headers)                              #res의 charset='EUC-KR'        #python의 인코딩과 다르네...so -> res.content.decode('euc-kr','replace')
text = res.content.decode('euc-kr','replace')    #res의 content를 'EUC-KR로 변경'   

soup = BeautifulSoup(text,'html.parser')
wholeFile = open('dataA.html','w',encoding='utf-8')
wholeFile.write(text)       #BeautifulSoup 형식 저장(x) -> text로 저장

#####HEAD####
stock_head = soup.find('thead').find_all('th')
stock_head_data = [head.get_text() for head in stock_head]  #List 안에서 for문 -> List형태로 저장
print(stock_head_data) 

#####STOCK_LIST####
stock_list = soup.find('table',attrs={"class":"type_2"}).find('tbody').find_all('tr')
for stock in stock_list:
    if len(stock)>1:
        print(stock.get_text().split())   #split() : 입력받은 문자를 기준으로 배열에 저장하여 RETURN 배열
