jumin = "911249-2018423"
print("성별 : " + jumin[7])
print("생년 : " + jumin[0:2])
print("월   : " + jumin[2:4])
print("생년월일 : " + jumin[:6])
print("생년월일2: " + jumin[0:-8])          #끝나는 인덱스 기준에 무조건 +1

python = "Python is amazing"
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")               #n문자가 들어간 index번호 찾기
print(index)
index = python.index("n", index+1)      #index+1의 자리에서부터 문자 n 검색
print(index)                    #find사용 결과값 출력: print(python.find("n"))


print(python.find("DB"))                #find 함수는 false일때 -1반환
#print(python.index("DB"))               #index 함수는 false일때 오류발생

print(python.count("n"))
