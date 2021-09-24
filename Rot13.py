word = input("Enter a word and a number: ")
for number in range(1,27,1):
    print("shift %d >> "%number,end='')
    for i in range(len(word)):
        if(word[i].isupper()):
            asciiNum = ord(word[i])-number
            if asciiNum<=64:
                asciiNum=90-(64-asciiNum)
            print("%c"%(asciiNum),end='')
        elif(word[i].islower()):
            asciiNum = ord(word[i])-number
            if asciiNum<=96:
                asciiNum=122-(96-asciiNum)
            print("%c"%(asciiNum),end='')    
        else:
            print(word[i],end='')
    print("")