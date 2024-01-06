text = "X-DSPAM-Confidence:    0.8475"
x = text.find("0")
lastnumber = text[x:]
lastnumber = float(lastnumber)
print(lastnumber)

#trying to find the number at the end of the string, convert it to a float, and print it