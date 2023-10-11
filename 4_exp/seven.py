import numpy as np
import statistics as stat
import random
list1 = []
n = int(input("Enter the size of sample:"))
for i in range(n):
    list1.append(random.uniform(0.0,1.0))
print("the sample data set:")
print(list1)
sampledata = np.array(list1)
print("mean:",np.mean(sampledata))
print("median:",np.median(sampledata))
print("standard deviation:",stat.stdev(sampledata))
print("variance:",stat.variance(sampledata))