import numpy as np

mat = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Column sums:", np.sum(mat, axis=0))
print("Row sums:", np.sum(mat, axis=1))