import difflib
def string_similar(str1,str2):
    result=difflib.SequenceMatcher(a=str1.lower(),b=str2.lower())
    return result.ratio()

str1=input("enter the first string:")
str2=input("enter the second string:")
print(string_similar(str1,str2))