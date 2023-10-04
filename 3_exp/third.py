def tower_of_hanoi(num , frompeg , topeg , auxpeg):
    if num == 1:
        print("the disk  is moved between {} and {}".format(frompeg,topeg))
        return
    tower_of_hanoi(num-1,frompeg,auxpeg,topeg)
    print("move  disk {} is moved between {} and {}".format(num,frompeg,auxpeg))
    tower_of_hanoi(num-1,auxpeg,topeg,frompeg)
print("Ronit Satish Mehta 60009230207")
n = int(input("enter the number of the disk"))
tower_of_hanoi(n,"A","C","B")


