print(" *** Max Min ***")
numList = input("Enter Number : ").split()
for i in range(len(numList)):
    numList[i] = int(numList[i])
print("list =",numList)
print("Max =",max(numList))
print("Min =",min(numList))