dictionary = {"V": 10, "VI": 10, "VII": 40, "VIII": 20, "IX": 70, "X": 80, "XI": 40, "XII": 20}

print("Original dictionary: ", dictionary)

result = {}

for x in dictionary.values():
    if x in result:
        result[x] = result[x] + 1
    else:
        result[x] = 1

print("Counter frequency of dictionary: ", result)