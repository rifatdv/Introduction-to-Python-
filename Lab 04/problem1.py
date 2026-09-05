d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

result = {}

for x in d2:
    result[x] = d2[x]

for x in d1:
    if x in result:
        result[x] = result[x] + d1[x]
    else:
        result[x] = d1[x]

print("Output: ", result)