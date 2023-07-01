num=[13,56,24,23,88,96,56]
num.append(00)#insert elemnts at the end
print(num)
num.sort()#sort asending order
print(num)
num.sort(reverse=True)
print(num)#sort descending order
num.reverse()
print(num)
n=num.index(56)#value index print
print(n)
m=num.count(56)#count the number of the 56 in the list
print(m)
num.insert(1,0)#insert the elemnt at the specific index
print(num)
x=[10,20,30,40]
y=["vinay","deepak"]
x.extend(y)# add an entire list or any other collecton of datatypes
print(x)
print(x+y)# concatenation of the to list
