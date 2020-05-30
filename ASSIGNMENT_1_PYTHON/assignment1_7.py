start = int(input("Enter the start range: "))
end = int(input("Enter the end range: "))
l = []

for i in range(start,end):
    n = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        r = temp % 10
        sum += r**n
        temp = temp // 10

    if (sum == i):
        l.append(i)
        
print("armstrong number in given range are :",l)
