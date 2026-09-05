import numpy as np

arr = np.array([2, 5, 7, 5, 9, 5, 3, 5])

item = 5
n = 3

indices = np.where(arr == item)[0]

if len(indices) >= n:
    print("Index of", n, "th repetition:", indices[n-1])
else:
    print("The item does not repeat", n, "times.")