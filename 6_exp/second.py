result = 0.0
try:
    print("Ronit Satish Mehta 60009230207")
    print("Computing ((a+d)+(b*c)/(b*d))")
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    c = int(input("Enter C:"))
    d = int(input("Enter D:"))
    result=((a+d)+(b*c)/(b*d))
except ZeroDivisionError:
    print("Divide by Zero not possible")
except ArithmeticError:
    print("Arithmetic error")
except FloatingPointError:
    print("Value not correct")
else:
    print("the result:",result)