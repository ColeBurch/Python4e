largest = None
smallest = None
while True :
    x = input("Enter a number: ")
    if x == "done":
        break
    try:
        x = int(x)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = x
    if smallest is None:
        smallest = x
    if x > largest :
        largest = x
    if x < smallest :
        smallest = x
print("Maximum is", largest)
print("Minimum is", smallest)