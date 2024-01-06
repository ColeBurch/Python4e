import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import lxml

url = input("Enter url - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

numlist = list()
tags = soup("span")
for tag in tags :
    num = tag.contents[0]
    intnum = int(num)
    numlist.append(intnum)

print("count", len(numlist))
print("sum", sum(numlist))