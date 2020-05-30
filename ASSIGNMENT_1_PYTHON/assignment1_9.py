
def divisors(n):
    div = []
    for i in range(1,n+1):
        if n % i == 0:
            div.append(i)
    #print(div)
    l = len(div)
    #print(l)
    sum = 0
    for j in div:
        sum += 1.0/j
    t = l / sum
    if round(t, 6).is_integer():
        print(n)

n = int(input("enter a number upto which you want harmonic divisors number : "))
for i in range(1,n):
    divisors(i)
