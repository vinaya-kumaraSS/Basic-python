num=[10,339,7,8,5]
def abc(x):
    return x>10 
newnum=filter(abc,num)
print(list(newnum))