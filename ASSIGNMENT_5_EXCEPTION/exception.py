#-----------------------KeyboardInterrupt error--------------------------------
print("----------KeyboardInterrupt error section------------")
try:
    inp = input(" ")

except KeyboardInterrupt as k:
    print('\nCaught the KeyboardInterrupt exception\n')
    print("ERROR : ",k)

else:
    print('No exception occurred')
print()
print()

#--------------------------ZeroDivisionError---------------------------------------
print("-----------ZeroDivisionError----------")
a = int(input("enter a dividend : "))
while(1):
    try:
        b = int(input("enter a divisor : "))
        ans = a/b


    except ZeroDivisionError as z:
        print("YOU CAN NOT DIVIDE A NUMBER BY ZERO !!!!!!")
        print("ERROR : ",z)
        print("Enter the divisor again.....")

    else:
        print("congrats your program succesfully run without getting an any error ....!")
        print("Result = ",ans)
        break
print()
print()
#--------------------------AssertionError----------------------------
print("----------assertionerror section------------")
try:
    a = 20
    b = 'suraj'
    assert a == b

except AssertionError:
    print("ERROR : assretion error occured!!!!! ")

else:
    print("Assertiontion occured succesfullly....")

print()
print()
#-----------------------------KeyError--------------------------------------
print("------KEY ERROR SECTION-------")

try:
    d = {1:'c', 2:'o', 3:'e', 4:'e',5:'p'}
    i = int(input("enter the value of key in the dictionary : "))
    print("result : ",d[i])

except KeyError as key:
    print("Entered key is not present in the dictionary")

else:
    print("No error while accesing the value of the key.")

print()
print()

#------------------------index error ----------------------
print("----------------index error section-------------------")

try:
    list = [1,2,3,4,5,6,7]
    i = int(input("Enter the index number of the list : "))
    print("result : ",list[i])

except IndexError as ie:
    print("Entered index is invalid!!!!!")
    print("ERROR :",ie)

else:
    print("NO error while accesing the list")

