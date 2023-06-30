name = input("Enter the name: ")
j = 0
k = 0
for i in name:
    if i == 'A' or i == 'I' or i == 'O' or i == 'U' or i == 'E' or i == 'a' or i == 'i' or i == 'o' or i == 'u' or i == 'e':
        j = j + 1
    else:
        k = k + 1
print("Number of vowels:", j)
print("Number of non-vowels:", k)