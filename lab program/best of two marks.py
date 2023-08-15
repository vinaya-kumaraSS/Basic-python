marks1=int(input("enter the first marks:"))
marks2=int(input("enter the second marks:"))
marks3=int(input("enter the third marks"))
if marks1>marks2:
    if marks2>marks3:
        total=marks1+marks2
    total=marks1+marks3
elif marks1>marks3:
    total=marks1+marks2
else:
    total=marks2+marks3
avg=total/2
print("the average of the best two marks is",avg)