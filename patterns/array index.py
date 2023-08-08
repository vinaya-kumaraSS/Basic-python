n=int(input("enter the number of rows:"))
m=int(input("enter the number of columns:"))
for i in range(1,n+1):
    print(f"{i} row")
    for j in range(1,m+1):
        print(f"{[i]}{[j]}\t")
