currency = {}
print("Ronit Satish Mehta 60009230207")
n = int(input("Enter the number of the currencys to enter"))
for i in range(n):
    country = str(input("Enter the currency name:"))
    currency1 = float(input("Enter the currency conversion:"))
    currency[country] = currency1
for i in currency:
    print(i,":",currency[i])