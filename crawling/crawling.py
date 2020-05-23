from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

baseURL = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
plusURL = input("검색어를 입력하세요 : ")

# 한글 검색 자동 변환, URL = baseURL + 검색어
URL = baseURL + quote_plus(plusURL)
html = urlopen(URL)
soup = bs(html, "html.parser")
img = soup.find_all(class_='_img')

n = 1
for i in img:
    imgURL = i['data-source']
    with urlopen(imgURL) as f:
        with open('./img/' + plusURL + str(n)+'.jpg','wb') as h: 
        # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
print("다운로드 완료")