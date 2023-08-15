number=int(input("enter the integer:"))
temp=number
str_val=str(number)
revese=0
while (number>0):
    dig=number%10
    revese=revese*10+dig
    number=number//10
    print("the reverse number is",revese)
if temp==revese:
    print("the number is palindrome")
else:
    print("the number is  not palindrome")
for i in range(10):
    count = str_val.count(str(i))
    if count > 0:
        print(f"{i} appears {count} times")