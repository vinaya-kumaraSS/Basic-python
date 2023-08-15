sentence=input("enter the sentence:")
w,l,u,d=0,0,0,0
l_w=sentence.split(" ")
word=len(l_w)
for i in sentence:
    if i.isdigit():
        d=d+1
    elif i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
print(f"lower:{l}")
print(f"uppre:{u}")
print(f"digit:{d}")
print(f"words:{word}")