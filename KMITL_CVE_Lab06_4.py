print(" *** Maximum value ***")
stringNum = input("Enter some numbers: ")
lstNum = stringNum.split(' ')
for i in range(len(lstNum)):
    lstNum[i]=float(lstNum[i])
print("Max value =", max(lstNum))