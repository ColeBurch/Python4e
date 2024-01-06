import re
fname = input("Enter a file name:")
fh = open(fname)
numlist = list()
for line in fh :
    list = re.findall("[0-9]+", line)
    if len(list) == 0 :
        continue
    for number in list :
        integer = int(number)
        numlist.append(integer)

print(sum(numlist))