import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter url - ')
xml = urllib.request.urlopen(url).read()

parsed = ET.fromstring(xml)
lst = parsed.findall('comments/comment')
numlist = list()
for item in lst :
    x = item.find('count').text
    x = int(x)
    numlist.append(x)

print(sum(numlist))