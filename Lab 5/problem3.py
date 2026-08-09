numbers=[5,10,20,50,25,15,30,7,2]

max = numbers[0]
min = numbers[0]

for num in numbers:
    if num > max:
        max = num
    if num < min:
        min = num

print("Maximum value: ", max)
print("Minimum value: ", min)