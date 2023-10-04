def func(num):
    if num == 1 or num == 0:
        return 1
    else:
       return num * func(num-1)
print("Ronit Satish Mehta 60009230207")
num = int(input("enter the number to find the factorial:"))
fact = func(num)
print("the factorial of the given number is:",fact)