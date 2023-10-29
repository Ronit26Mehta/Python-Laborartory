with open(r"C:\Users\mehta\OneDrive\Documents\GitHub\Python-Laborartory\9_exp\h1.txt", 'r') as f:
    f  = f.readline()
    for i in f:
        words = i.split()
        for j in words:
            print(j+"#")
