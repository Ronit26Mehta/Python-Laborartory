import numpy as np
import random
import statistics as stats
list1 = []
class first():
    def calculate(self,n):
        self.b = []
        for i in range(n):
         self.b.append(random.uniform(0.0,1.0))
class second(first):
   def display(self,n):
      self.b = np.array(self.b)
      self.y = []
      print("the data:")
      print(self.b)
      for i in range(n):
        self.y.append(random.uniform(0.0,1.0))
      self.y=np.array(self.y)
      print("the mean:",np.mean(self.b))
      print("the median:",np.median(self.b))
      print("the linear regression:",stats.linear_regression(self.b,self.y))
      print("the mode:",stats.mode(self.b))
      print("the variance:",stats.variance(self.b))
      print("the covariance:",stats.covariance(self.b,self.y))
      print("the standard deviation:",stats.stdev(self.b))
print("Ronit Satish Mehta 60009230207")
s = second()
n = int(input("Enter the number to generate data:"))
s.calculate(n)
s.display(n)