countries=("india","china","japan","usa")
temp=list(countries)            #convert tuple to list
temp.append("shrilanka")        #insert element in last
temp.pop(4)                     #remove the element at specific index
temp[2]="aaaa"                  #insert at specific index
countries=tuple(temp)           #convert list to tuple
print(countries)