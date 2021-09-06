print(" *** integer summation from 1 to n ***")
num = input("Enter an integer(n) : ")
num = int(num)
print("Summation => ",end='')
sum = 0                     #Find summation
for i in range(1,num+1):
    if i==num: 
        print(i,end=' = ')
    else:
        print(i,end='+')
    sum+=i
print(sum)