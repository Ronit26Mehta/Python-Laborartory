n1 = 0
n2 = 1
count = 0
print("Ronit Satish Mehta sap ID: 60009230207")
n = int(input("enter the amount of the numbers to print"))
print(1)
while(count < n):
    nth_term = n1 + n2 
    n1 = n2
    n2 = nth_term
    print(nth_term)
    count += 1