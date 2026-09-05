sample = [10,20,30,30,30,30,20,40]
print("Sample List: ", sample)

def distinct(numbers):
    count = {}

    for x in numbers:
        if x in count:
            count[x] = count[x] + 1
        else:
            count[x] = 1

    for value in count:
        print(value, " => ", count[value])

distinct(sample)