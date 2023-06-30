import random
a=int(input("enter the number between 1 to 10:"))
rand=random.randint(1,10)
print("generated number is :",rand)
if a==rand:
    print("your prediction is correct")
else:
    print("your prediction is incorrect")

