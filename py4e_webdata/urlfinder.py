import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import lxml

url = input('Enter url - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

tags = soup('a')
for tag in tags :
    print(tag.get('href', None))