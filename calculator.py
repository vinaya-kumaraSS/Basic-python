def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return(a/b)
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4,division")
choice=int(input("enter your choice"))
if choice==1:
    print("addition :",add(a,b))
elif choice==2:
    print("substraction :",sub(a,b))
elif choice==3:
    print("multiplication :",mul(a,b))
elif choice==4:
    print("division :",div(a,b))
else:
    print("enter the valid choice")
