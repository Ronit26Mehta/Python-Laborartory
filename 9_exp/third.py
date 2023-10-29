import os
file_size =0
file_path =r"C:\Users\mehta\OneDrive\Documents\GitHub\Python-Laborartory\9_exp\alanturing.txt"
if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    line_count = 0
    word_count = 0
    character_count = 0
    with open(file_path,'r') as f:
        for i in f:
            line_count+=1
            line = i.split()
            word_count+=len(line)
            character_count+=len(i)
    print("Ronit Satish Mehta 60009230207")
    print("the file size:",file_size)
    print("the line count:",line_count)
    print("the character count:",character_count)
    print("the word count:",word_count)
