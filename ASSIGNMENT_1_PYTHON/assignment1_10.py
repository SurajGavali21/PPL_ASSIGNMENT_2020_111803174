import math
print("Enter the properties of the geometric series you want")
a = int(input("Enter first number : "))
r = int(input("Enter ratio : "))
n = int(input("How many numbers you want : "))

def gp(a,r,n):
    for i in range(0,n):
        term = a * pow(r,i)

        print(term, end="\n")

print("geometric series with entered properties is :")
gp(a,r,n)
print()