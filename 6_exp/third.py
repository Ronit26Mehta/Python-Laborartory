class muliplied_by_zero_error(Exception):
    pass
result = 0
try:
    print("Ronit Satish Mehta 60009230207")
    b = int(input("Enter the value of b"))
    d = int(input("Enter the value of d"))
    result = (b*d)
    if result == 0:
        raise muliplied_by_zero_error
except muliplied_by_zero_error:
    print("anyting mulitplied by zero would give you zero")
else:
    print("the reuslt is:",result)