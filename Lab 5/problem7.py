words = ['aca', 'xyz', 'aba', '1221']
count = 0

for x in words:
    if len(x) >= 2 and x[0] == x[-1]:
        count += 1
print("Count:", count)