import requests
from bs4 import BeautifulSoup



url = "https://finance.naver.com/sise/sise_market_sum.nhn"

res = requests.get(url, headers={'User-Agent':'Mozila/5.0'})
print(res.headers)                              #res의 charset='EUC-KR'
text = res.content.decode('utf-8','replace')    #res의 content를 'UTF-8로 변경'   

soup = BeautifulSoup(text,'html.parser')
wholeFile = open('dataA.html','w',encoding='utf-8')
wholeFile.write(text)       #BeautifulSoup 형식 저장(x) -> text로 저장
