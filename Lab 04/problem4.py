sample = [1,2,3,3,3,3,4,5]
print("Sample List: ", sample)

def distinct(numbers):
    list = []

    for x in numbers:
        if x not in list:
            list.append(x)

    return list

print("Sample Output: ", distinct(sample))