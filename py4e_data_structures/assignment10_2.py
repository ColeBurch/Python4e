#Write a program to read through the mbox-short.txt and figure out the distribution 
#by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time 
#and then splitting the string a second time using a colon.
#"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour
#04 3
#06 1
#etc...
fname = input("Enter a file name ")
fh = open(fname)
hours = dict()
for lines in fh :
    if not lines.startswith("From ") :
        continue
    words = lines.split()
    time = words[5]
    time = time.split(":")
    hour = time[0]
    hours[hour] = hours.get(hour, 0) + 1

for k,v in sorted(hours.items()) :
    print(k, v)