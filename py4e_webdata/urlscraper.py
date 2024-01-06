import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import lxml

url = input("Enter url - ")
iterate = input("Enter count - ")
iterate = int(iterate)
position = input("Enter Position - ")
position = int(position) - 1
count = 0

while count is not iterate :
    taglist = list()
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    tags = soup('a')
    for tag in tags :
        taglist.append(tag.get('href', None))
    print(taglist[position])
    url = taglist[position]
    count = count + 1