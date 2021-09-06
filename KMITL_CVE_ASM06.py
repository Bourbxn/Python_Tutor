row,col=input("Enter Rows Columns : ").split()
row=int(row)
col=int(col)
word = "KMITL"
for i in range(row):
    for j in range(col):
        print(word,end=' ')
    print()