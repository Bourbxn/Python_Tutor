from typing import Text

# Fuction
def findDict(text):
    dict = {}
    for i in range(len(text)):
        cout = 0
        for j in range(len(text)):
            if text[i] == text[j]:
                cout += 1
        dict[text[i]] = cout
    return dict


# Input
text = input().split(" ")
for i in range(len(text)):
    print(text[i], end=" = ")
    print(findDict(text[i]))

if len(text) > 1:
    stringMerge = ""
    stringMergeFind = ""
    for i in range(len(text)):
        stringMerge += text[i]
        stringMergeFind += text[i]
        if i != len(text) - 1:
            stringMerge += " "
    print(stringMerge, "= ", end="")
    print(findDict(stringMergeFind))
else:
    stringMergeFind = text[0]

# Find Max
print("Maximum Character Count: ", end=" ")
maxKey = max(findDict(stringMergeFind), key=findDict(stringMergeFind).get)
maxValue = max(findDict(stringMergeFind).values())
print(maxKey, end=" ")
print(maxValue)
