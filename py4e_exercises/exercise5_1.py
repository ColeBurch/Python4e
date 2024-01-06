count = 0
sum = 0
while True :
    x = input("Enter a number: ")
    try:
        if x == "done" :
            break
        else:
            x = int(x)
            sum = sum + x
            count = count + 1
    except:
        print("Invalid Input")
print(sum, count, sum/count)