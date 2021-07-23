#-*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame as df


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


stockTop50_crop = soup.find('table',attrs={"class":"type_2"}).find('tbody').find_all('a',attrs={"class":"tltle"})
for index, stock in enumerate(stockTop50_crop):
    link="https://finance.naver.com"+stock["href"]
    sub_res = requests.get(link)
    sub_resp = sub_res.content.decode('euc-kr','replace')
    sub_soup = BeautifulSoup(sub_resp,'html.parser')


##function getDataOfParam()
def getDataOfParam(param):
    print(param)
    sub_tbody = sub_soup.find("table", "tb_type1 tb_num tb_type1_ifrs").find('tbody')
    sub_title = sub_tbody.find('th',param).find('strong').get_text()
    dataOfParam = sub_tbody.find('th',param).parent.find_all('td')          #sub_tbody.find('th',param)의 부모클래스의 td받아오기
    value_param = [i.get_text().strip() for i in dataOfParam]
    #print(sub_title, ":",value_param)
    return value_param

ParamList = ['매출액','영업이익','당기순이익','ROE(지배주주)','PER(배)','PBR(배)']
for idx, pText in enumerate(ParamList):
    param=' '.join(sub_soup.find('strong',text=pText).parent['class'])      #ParamList가 '영업이익' 일때, pText도 '영업이익이면' list형태로 출력
    getDataOfParam(param)   #param (h_th2 th_cop_anal9 -> h_th2th_cop_anal9로 띄어쓰기 생략)

# sub_thead = sub_soup.find("table",attrs={"class":"tb_type1 tb_num tb_type1_ifrs"}).find('thead').find_all("th",attrs={"scope":"col","class":""})
# print("최근연간실적 :", [i.get_text().strip() for i in sub_thead])





##json 형태로 출력##



#i.get_text().strip()  strip형태로 출력
#iterable:  member를 하나씩 차례로 반환 가능한 object(list, str, tuple)