# https://www.crummy.com/software/BeautifulSoup/
#https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/networking-web-scraping-with-python

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - http://www.dr-chuck.com/page1.htm')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))