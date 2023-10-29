class invalid_marks(Exception):
    pass
try:
    print("MARKS CHECKER")
    print("Ronit Satish Mehta 60009230207")
    n = int(input("Enter your marks"))
    if n>100:
        raise invalid_marks
except invalid_marks:
    print("illegal marks entry")
else:
    print("Marks are right")