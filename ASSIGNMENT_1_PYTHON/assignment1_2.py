import random

n = int(input("for rolling dice press 1 : "))
number = random.randint(1, 7)
print("you get number : {}".format(number))

def dice():
    while True:
        print()
        ans = str(input("Do you want to continue rolling dice?\n if YES then press 'y' , if no then press 'n'  :  "))

        if ans == "y":
            number = random.randint(1,6)
            print("you get number : {}".format(number))

        else:
            print()
            print("game exited....")
            return
dice()
