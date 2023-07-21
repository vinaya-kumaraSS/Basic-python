try:
    list=[10,20,30]
    pos=int(input("enter the index:"))
    print(list[pos])
except:
    print("index element is not found")
finally:
    print("execution completed")