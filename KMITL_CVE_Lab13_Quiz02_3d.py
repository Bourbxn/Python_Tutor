num = int(input("Please enter a positive integer value : "))
# top
for i in range(num):
    print(" " * i, end="")
    print("\\", end="")
    print(" " * (num - i), end="")
    print("|")
# mid
print(" " * num, end="")
print(">|")
# Bottom
for i in range(num):
    print(" " * (num - i - 1), end="")
    print("/", end="")
    print(" " * (i + 1), end="")
    print("|")
