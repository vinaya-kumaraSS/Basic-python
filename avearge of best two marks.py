m1=int(input("enter the marks of first test:"))
m2=int(input("enter the marks of second test:"))
m3=int(input("enter the marks of third test:"))
if m1>m2:
    if m2>m3:
        total=m1+m2
    else:
        total=m1+m3
elif m1>m3:
    total=m1+m2
else:
    total=m2+m3
avg=total/2
print("the average of best two mark is",avg)