sum = 0
count = 0
while True :
    x = input("Enter a number: ")
    if x == "done" :
        break
    try:
        x = int(x)
    except:
        print("Invalid Input")
        continue
    sum = sum + x
    count = count + 1
print(sum, count, sum/count)