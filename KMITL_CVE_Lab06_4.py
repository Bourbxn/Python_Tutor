print(" *** Maximum value ***")
stringNum = input("Enter some numbers: ")
lstNum = stringNum.split(' ')
for i in range(len(lstNum)):
    lstNum[i]=float(lstNum[i])
maxValue = max(lstNum)
if int(maxValue) == maxValue:
    maxValue = int(maxValue)
print("Max value =", maxValue)