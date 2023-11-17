result = ""
list_name = ["vishnu", "vishal", "visay"]
list_name.sort()

first = list_name[0]
last = list_name[len(list_name) - 1]

for i in range(0, len(first)):
    if first[i] != last[i]:
        break
    else:
        result =result+ first[i]

print(result)
