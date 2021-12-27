print(" *** Adding number ***")
lst = input().split(" ")
for i in range(len(lst)):
    lst[i]+=str(int(i+1))
print(lst)
for i in lst:
    print(i,end=' ')