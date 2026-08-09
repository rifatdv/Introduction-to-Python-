numbers = [10,20,30,20,50]
print("Sample List: ", numbers)

for x in range(len(numbers)):
    if numbers[x] == 20:
        numbers[x] = 200


print("Expected Result ", numbers)
