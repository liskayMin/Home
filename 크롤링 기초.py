f = open("test.txt","w", encoding="utf8") # w는 다시 씀
f.write("ㅎㅇ")

f = open("test.txt","a", encoding="utf8") # a 는 추가
f.write("ㅎㅇ")

f = open("test.txt","a", encoding="utf8") # a 는 추가
f.write("ㅎㅇ\n")

f = open('test.txt', 'r', encoding="utf-8")
print(f.read())

f.seek(11) # 11로 위치 조정 가능

print(f.readline()) # 한 줄만

print(f.readlines())

--------------------------------------------------------

fr = open('test.txt','rb')
fw = open('test_copy.txt','wb')
data = fr.read()
print(data.decode('utf8'))
print(data)
fw.write(data)

fr.close()
fw.close()

--------------------------------------------------------

fr = open('1.png','rb')
fw = open('1_copy.jpg','wb')
fw.write(fr.read())

fw.close()
fr.close()

--------------------------------------------------------

with open('1.png', 'rb') as fr:
    with open('2.png','wb') as fw:
        fw.write(fr.read())  # 이렇게 하면 close 안해줘도 됨

--------------------------------------------------------

다음사이트에서 사진 가져오기
import urllib.request as req

rep = req.urlopen('https://daum.net')

print(rep.getheaders()) # getheaders
print(rep.getheaders("Date"))

print(rep.status) # 200은 정상작동

f = open('daum.html','w',encoding='utf8')
f.write(rep.read().decode('utf8'))
f.close()

import re 

data = rep.read().decode('utf8')

result = re.findall('https://[./-_\w]+.jpg',data) # \w는 모든 문자 0-9a-zA-Z 할 필요 없음
for link in result:
    idx = link.rfind('/') # rfind 는 right find로 오른쪽부터 찾음
    with open(link[idx+1:],'wb') as f: # idx 다음부터 제목이 되게
        pic = req.urlopen(link)
        f.write(pic.read())

--------------------------------------------------------

from bs4 import BeautifulSoup
import urllib.request as req

res = req.urlopen('https://finance.naver.com/news/mainnews.naver?date=2021-10-08')

soup = BeautifulSoup(res, 'html.parser')

print(soup.find('div')['id']) # 딕셔너리처럼 뽑아 올 수 있음 
class는 _ 해줘야함

print(soup.find_all('a')) # 리스트로 가져옴

for tag in soup.find_all('a'):
    print(tag['href'])

result = soup.select('#contentarea_left > div.mainNewsList') # id가 첫번쨰, div가 두번째 인 애를 select 하겠다는 것
for tag in result:
    print(tag['href'])
print(result)

--------------------------------------------------------

