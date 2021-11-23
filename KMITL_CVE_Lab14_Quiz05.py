text = input("Enter age and name : ").split(" ")
# List
print(text)
# dict
dict = {}
for i in range(len(text) // 2):
    dict[text[i * 2 + 1]] = int(text[i * 2])
print(dict)
# tuple
tupl = list(dict.items())
print(tupl)
# tuple sort
tupl.sort(reverse=True)
print(tupl)
# Histrogram
print("*** The Histogram of Age ***")
for i in range(len(tupl)):
    print(tupl[i][0][0:3], ":", end=" ")
    print("=" * (int(tupl[i][1])), end="")
    print(int(tupl[i][1]))
