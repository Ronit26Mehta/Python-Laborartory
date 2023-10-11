import numpy as np
from statistics import mode  
array = np.array([2,3,5,6,8,9,8,6,3,35,6])
frequent_value = mode(array)
print("the value is:",frequent_value)