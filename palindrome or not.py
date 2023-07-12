number=int(input("enter the number:"))
temp=number
str_val=str(number)
reverse=0
while(number>0):
    dig=number%10
    reverse=reverse*10+dig
    number=number//10
    print("the reverse number is:",reverse)
if temp==reverse:
    print("the number is palindrime")
else:
    print("the number is not palindrime")
for i in range(10):
    if str_val.count(str(i))>0:
        print(str(i),"appears",str_val.count(str(i)),"times")
        

    
