import numpy as np
list1 = []
matrix1 = np.array([[1,2,3,4],[3,4,5,7],[2,4,6,7]])
n = int(input("Enter the size of row:"))
for i in range(n):
    m = int(input())
    list1.append(m)
print(list1 in matrix1.tolist())
