largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fval = int(num)
    except:
        print('Invalid input')
        continue
    
    if largest is None or fval > largest:
        largest = fval
    if smallest is None or fval < smallest:
        smallest = fval

print("Maximum is", largest)
print("Minimum is", smallest)