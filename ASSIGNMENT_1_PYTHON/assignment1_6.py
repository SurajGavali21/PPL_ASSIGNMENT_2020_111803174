
def divisor_sum(x):
    #l = []
    sum = 1
    for i in range(2,x) :
        if x % i == 0:
            sum = sum + i
            #l.append(i)

    return sum

#result = divisor_sum(66)
#print(result)

def is_ammicable(a,b):
    if divisor_sum(a) == b and divisor_sum(b) == a:
        #print("{} and {} are amicable".format(a,b))
        return a,b
    else:
        False

def print_pairs(n):
    for i in range(0,n):
        for j in range(i+1,n):
            if is_ammicable(i,j):
                print(i,j)

n = int(input("Enter the value upto which you want ammicable numbers : "))
print_pairs(n)