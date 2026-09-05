numbers = [10,20,30,20,50]
print("Sample List: ", numbers)

unique = []

for x in numbers:
    if x not in unique:
        unique.append(x)

print("Expected Result ", unique)