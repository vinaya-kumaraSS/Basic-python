n=input("enter integer:")
try:
    for i in range(1,11):
        print(f"{int(n)}x{i}={int(n)*i}")
except:
    print("invalid input")