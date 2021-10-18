print(" *** Adding number ***")
lst = input().split(" ")
print(lst)
for i in range(len(lst)):
    lst[i]+=str(int(i+1))
print(lst)