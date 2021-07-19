#-*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup



url = "https://finance.naver.com/sise/sise_market_sum.nhn"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

res = requests.get(url, headers=headers)            

#print(res.headers)                              #res의 charset='EUC-KR'        #python의 형태는 
text = res.content.decode('euc-kr','replace')    #res의 content를 'EUC-KR로 변경'   

soup = BeautifulSoup(text,'html.parser')
wholeFile = open('dataA.html','w',encoding='utf-8')
wholeFile.write(text)       #BeautifulSoup 형식 저장(x) -> text로 저장

