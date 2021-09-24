print(" *** Maximum value ***")
stringNum = input("Enter some numbers: ")
lstNum = stringNum.split(' ')
for i in range(len(lstNum)):
    lstNum[i]=int(lstNum[i])
print("Max value =", max(lstNum))