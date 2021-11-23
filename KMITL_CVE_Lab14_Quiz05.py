text = input("Enter age and name : ").split(" ")
# List
print(text)
# dict
dict = {}
for i in range(len(text) // 2):
    dict[text[i * 2 + 1]] = int(text[i * 2])
print(dict)
#tuple
tupl = list