lst = input().split(",")
print("    A B C D")
lstOrder = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(len(lst)):
    row = 0
    collumn = 0
    # Check row
    if lst[i][0] == "A":
        row = 0
    elif lst[i][0] == "B":
        row = 1
    elif lst[i][0] == "C":
        row = 2
    elif lst[i][0] == "D":
        row = 3
    # Check collumn
    if lst[i][2] == "A":
        collumn = 0
    elif lst[i][2] == "B":
        collumn = 1
    elif lst[i][2] == "C":
        collumn = 2
    elif lst[i][2] == "D":
        collumn = 3
    lstOrder[row][collumn] = 1
posabcd = 0
for i in lstOrder:
    print("%c" % (65 + posabcd), end=" ")
    print(": ", end="")
    poscomma = 0
    for j in i:
        print(j, end="")
        if poscomma != 3:
            print(",", end="")
        poscomma += 1
    print()
    posabcd += 1
