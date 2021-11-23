text = input("Enter : ").split(" ")
dict_old = {"Volkswagan": 1, "Toyota": 2, "Tesla": 2}
print("dict_old =", dict_old)
for i in range(len(text) // 2):
    print(text[i * 2], "exists in dicts")
# Create new dict
for i in range(len(text) // 2):
    if text[i * 2] in dict_old:
        dict_old[text[i * 2]] += int(text[i * 2 + 1])
    else:
        dict_old[text[i * 2]] = int(text[i * 2 + 1])
print("dict_new =", dict_old)
