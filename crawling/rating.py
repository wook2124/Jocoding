#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus

URL = "https://www.daum.net/"

html = urlopen(URL)

soup = bs(html, 'html.parser', from_encoding='utf-8')
i = 1
f = open("rating.txt", 'w')
for anchor in soup.select("a.link_favorsch"):
    data = (str(i) + "위 : " + anchor.get_text() + "\n")
    i = i + 1
    f.write(data)
f.close()