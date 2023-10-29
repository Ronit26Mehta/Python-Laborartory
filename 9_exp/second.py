import os
choice = 0
while choice != -1:
    if os.path.exists(r"C:\Users\mehta\OneDrive\Documents\GitHub\Python-Laborartory\9_exp\data.txt"):
        print("File for data is their")
    else:
        print("File is not their for data")
    print("Ronit Satish Mehta 60009230207")
    print("DATA ENTRY")
    print("1.ACCEPT")
    print("2.DISPLAY")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        name = str(input("Enter Name:"))
        roll_no = str(input("Enter Roll:"))
        data ="\n"+name+"\t"+roll_no+"\n" 
        with open("data.txt",'a+') as f:
            f.write(data)
    elif choice ==2:
        with open("data.txt","r") as f:
            for i in f.readlines():
                print(i.strip())

