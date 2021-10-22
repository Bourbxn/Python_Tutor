print(" *** Median Mean ***")
numList = input("Enter Number : ").split()
sum = 0
#Change to int list
for i in range(len(numList)):
    numList[i] = int(numList[i])
print("list =",numList)
#Find Mean
mean = 0
for i in range(len(numList)):
    sum+=numList[i]
if(sum%len(numList)==0):
    mean = sum//len(numList)
elif(sum%len(numList)!=0):
    mean = sum/len(numList)
print("Mean =",mean)
#Sort List
numList.sort()
print("sort list =",numList)
#Median
median = 0
posMid1 = 0
posMid2 = 0
if(len(numList)%2==0):
    posMid1 = (len(numList)//2)-1
    posMid2 = (len(numList)//2)
    median = numList[posMid1]+numList[posMid2]
    if(median%2==0):
        median//=2
    else:
        median/=2
else:
    posMid1 = ((len(numList)+1)//2)-1
    median = numList[posMid1]
if(median==int(median)):
    print("Median = ",median)
else:
    print("Median = %.2f"%median)