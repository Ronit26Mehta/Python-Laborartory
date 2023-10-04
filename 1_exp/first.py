list1 = ["Rogério Ceni","Bebeto","Alfrédo Di Stefano","David Silva","Arjen Robben","David Luiz","David Alaba","Jamie Vardy","Sergio Agüero","Frenkie de Jong"]
print("Ronit Satish Mehta 60009230207")
print(list1)
for i in range(len(list1)):
    print(i,list1[i])
list1.sort()
print("the sorted list:")
for i in range(len(list1)):
    print(i,list1[i])
list1.remove("Alfrédo Di Stefano")
print("After removal")
for i in range(len(list1)):
    print(i,list1[i])
