print(" *** Sequence Verification ***")
numList = input().split(" ")
asCheck = 0
deCheck = 0
for i in range(len(numList)-1):
    if(int(numList[i])>int(numList[i+1])):
        deCheck += 1
    elif(int(numList[i])<int(numList[i+1])):
        asCheck += 1
if(deCheck==len(numList)-1):
    print("Descending sequence !!!")
elif(asCheck==len(numList)-1):
    print("Ascending sequence !!!")
else:
    print("Neither ascending or descending sequence !!!")
