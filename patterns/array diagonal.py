n=int(input("enter the number of rows:"))
m=int(input("enter the number of columns:"))
if n==m:
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(i==j):
                print(i)
                print('\t')
            else:
                print(0)
                print('\t')
else:print("row and column are not equal")