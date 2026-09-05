num = int(input("Enter number: "))

a = 0
b = 1

while a< num:
    print(a, end=" ")
    c = a+b
    a = b
    b = c