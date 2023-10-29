print("Ronit Satish Mehta 60009230207")
source = input("Enter source:")
destination = input("Enter destination:")
with open(source,'r') as file1:
    with open(destination,'a') as file2:
        for i in file1:
            file2.write(i)
    print("Operation done")