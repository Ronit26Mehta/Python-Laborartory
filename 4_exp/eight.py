import numpy as np
matrix1 = np.array(["RonitMehta","60009230207"])
print("before operations:")
print(matrix1)
matrix2 = np.char.join(" ",matrix1)
print("after operations:")
print(matrix2)