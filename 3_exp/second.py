def mean(set):
    n = len(set)
    mean_ = sum(set)/ n
    print("the average of all the values is:",mean_)
set = []
print("Ronit Satish Mehta 60009230207")
n = int(input("enter the aritmetic variables to calculate mean:"))
print("Start entering Elements:")
for i in range(0,n):
   number = int(input())
   set.append(number)
mean(set)

