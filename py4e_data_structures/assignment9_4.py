#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input("Enter a file name: ")
fh = open(fname)
address = dict()
for line in fh :
    if not line.startswith("From ") :
        continue
    words = line.split()
    email = words[1]
    address[email] = address.get(email, 0) + 1

maxaddress = None
maxvalue = None
for k,v in address.items() :
    if maxvalue is None or v > maxvalue :
        maxaddress = k
        maxvalue = v

print(maxaddress, maxvalue)