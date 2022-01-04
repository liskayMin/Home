from bs4 import BeautifulSoup
import requests

code = 298020

for k in range(10):
    page = k + 1
    print('<page = '+ str(page)+'>')
    url = 'https://finance.naver.com/item/board.naver?code='+str(code)+'&page='+str(page)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    res = requests.get(url, headers = headers)

    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all('td', class_ = 'title')

    for i in range(len(title)):
        a = title[i].text
        b = a.splitlines()
        print(b[1])
    print('\n')