import numpy as np
matrix = np.array([[1,3],[3,4]])
print("before changing dimension")
print(matrix)
changed = matrix.reshape(1,4)
print(changed)