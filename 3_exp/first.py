def input_value(func,x):
    return func(x)
def  converter(x):
    return x*83
def get_mulitplier(factor):
    def mulitplier(x):
        return x * factor
    return mulitplier
print("Ronit Satish Mehta 60009230207")
n = int(input("Enter the value to convert:"))
print(input_value(converter,n))
p = int(input("Enter the value to factor:"))
q = int(input("Enter the muliplier"))
time_number = get_mulitplier(p)
result_time = time_number(q)
print("Main result",result_time)
