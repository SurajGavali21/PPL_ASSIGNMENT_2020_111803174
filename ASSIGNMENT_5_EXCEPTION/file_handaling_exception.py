
while(1):
    file = str(input("Enter the file name : "))

    try:
        filecontent = open(file, "r")
        content = filecontent.read()

    except FileNotFoundError as F:
        print("entered file doenit exist please check the spelling you entred. Try again!!!!")
        print("ERROR : ",F)

    else:

        print("File content: {}\n".format(content))
        print("file readed succesfully.............")
        break



