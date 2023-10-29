num1 = 0
num2 = 0
result = 0
try:
    num1 = int(input("Enter a value:"))
    num2 = int(input("Enter a value"))
    assert num1 and num2 != 0
except:
    print("Not possible")
else:
    result = num1 / num2
    print("the result is:",result)