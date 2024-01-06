import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url - ')
J = urllib.request.urlopen(url).read()

info = json.loads(J)
comment = info['comments']
numlist = list()
for item in comment :
    num = item['count']
    num = int(num)
    numlist.append(num)

print(sum(numlist))