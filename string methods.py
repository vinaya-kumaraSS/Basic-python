name1="vinay"
name2="KUMAR"
name3="@@@deepak@@@@@"
#strings are immutable-we cannot change 
print(name1.upper())#to upper case letter
print(name2.lower())#to lower csse letter
print(name3.rstrip("@"))#remove the special character(strip only the tail part)
print(name3.replace("deepak","darshan"))#replace the word
name4="subbu chandan barath"
name5="subbu*chandan*barath"
print(name4.split(" "))#split the words with space
print(name4.split("*"))#split the words with *
z="hi iam vinay"
print(z.capitalize())#capitalize the first letter and it will arrage & format
print(z.center(50))#align the z in a center with the space of 50
print(z.count("i"))#find the number of i the string
y="vinay23!"
print(y.endswith("!!"))#check the end with !! or not(return:true/false)
print(z.find("iam"))#find if the element is present or not, if present it gives index, not found return -1
print(z.index("aa"))#same as find() but it gives the error if the element is not found
print(y.isalnum())#it return true if the all the elements in the are A-Z, a-z,0-9
print(y.isalpha())#it return true if the all the elements in the string are A-Z, a-z
print(y.islower())#return true when all the character are lowercase
n="vinay\n"
print(n.isprintable())#return true when all the characetr are printable otherwise false
m="alvas institute of engineering and technology"
print(m.isspace())#check the white space
print(m.istitle())#returns true when all the characters are capital
print(m.startswith("alvas"))#return true when the letter are start with 'alvas'
c="AbCdE"
print(c.swapcase())#convert the lower to upper and upper to lower case
print(m.title())#convert the all first letter with capital
