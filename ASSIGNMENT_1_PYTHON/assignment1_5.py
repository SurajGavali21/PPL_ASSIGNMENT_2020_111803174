def missing(lst):
    lst1 = []
    for i in range(1,25):
        if i not in lst:
            lst1.append(i)
    return lst1
l = []

def input_list():
    count = 0
    while (count < 25):
        pageno = int(input("Enter page number(-1 to exit): "))

        if pageno == -1:
            break
        elif pageno > 25:
            print("Page number is greater than 25")
        elif pageno < 0:
            print("Page number cannot be negative(-1 to exit)")
        else:
            l.append(pageno)
            count += 1
    print("Entered pages number are : ", set(l))

    return l

lst = input_list()
#list1 = [2,4,6,12,16,17,20,21]
newlist = missing(lst)
print("missing pages are : ",newlist)
print()



