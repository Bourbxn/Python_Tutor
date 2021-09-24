word,number = input("Enter a word and a number: ").split()
number= int(number)
if (number < 1 or number >26):
    print("Number must be between 1-26")
else:
    for i in range(len(word)):
        if(word[i].isupper()):
            asciiNum = ord(word[i])-number
            if asciiNum<=64:
                asciiNum=90-(64-asciiNum)
            print("%c"%(asciiNum),end='')
        elif(word[i].islower()):
            asciiNum = ord(word[i])-number-32
            if asciiNum<=64:
                asciiNum=90-(64-asciiNum)
            print("%c"%(asciiNum),end='')