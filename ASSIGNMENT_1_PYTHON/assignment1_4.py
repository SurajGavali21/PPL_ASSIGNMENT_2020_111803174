import random
n = random.randint(1,100)
print("HINTS :")
if n % 2 == 0 :
    print("even number")
elif n%2 != 0 :
    print("odd number")

#print(n)
print("Guess a number choosed by me and the number is in between 1 to 100 !!!!(you have only 10 chances)")
print()
nog = 10
while nog < 11 :
    print("now you have only {} chance left!!!!".format(nog))
    number = int(input("enter a number : "))
    if number == n:
        print("congrats you guessed the correct number!!!")
        break

    elif number < n:
        print("choosen number is smaller than correct number")
        print()

    elif number > n:
        print("choosen number is greater than correct number")
        print()

    nog = nog - 1
    if nog == 0:
        print("no more attempts!!")
        break
print("correct number was : ",n)

