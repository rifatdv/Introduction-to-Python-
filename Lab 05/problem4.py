numbers = [10,20,30,40,50,60]

num = int(input("Enter a number to search: "))
found = False
for x in range(len(numbers)):
    if numbers[x] == num:
        print("Number is in the list.")
        found = True
        break

if not found:
    print("Number is not in the list")