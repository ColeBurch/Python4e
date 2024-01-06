score = input("Enter Score: ")
try:
    s = float(score)
    if s>1:
        print("out of range")
    elif s<0:
        print("out of range")
    elif s>=0.9:
        print("A")
    elif s>=0.8:
        print("B")
    elif s>=0.7:
        print("C")
    elif s>=0.6:
        print("D")
    else:
        print("F")
except:
    print("out of range")