print(" *** Find word start with character ***")
colorList=["yellow","red","green","black","brown","grey"]
colorListFound=[]
print(colorList)
char = input("Enter your character : ")
for i in colorList:
    if i[0]==char:
        colorListFound.append(i)
if len(colorListFound)==0:
    print("There is no element start with '%c'"%char)
else:
    print(colorListFound)
