#Function the multiple marks with credits
def marks_and_credits( marks, credits):
    if marks<=100 and marks>=90:
        return (10*credits)
        
    elif marks>=80 and marks<90:
        return (9*credits)
        
    elif marks>=70 and marks<80:
        return (8*credits)
    
    elif marks>=60 and marks<70:
        return (7*credits)
        
    elif marks>=55 and marks<60:
        return (6*credits)
        
    elif marks>=50 and marks<55:
        return (5*credits)
        
    elif marks>=40 and marks<50 :
        return (4*credits)
    
    elif marks>=0 and marks<40:
        print("fail")

#Inputs from the user    
MAT31=int(input("enter the 21MAT31 marks :"))
sub1=marks_and_credits(MAT31,3)

CS32=int(input("enter the 21CS32 marks :"))
sub2=marks_and_credits(CS32,4)

CS33=int(input("enter the 21CS33 marks :"))
sub3=marks_and_credits(CS33,4)

CS34=int(input("enter the 21CS34 marks :"))
sub4=marks_and_credits(CS34,3)

CSL381=int(input("enter the 21CSL381 marks :"))
sub5=marks_and_credits(CSL381,1) 

CSL35=int(input("enter the 21CSL35 marks :"))
sub6=marks_and_credits(CSL35,1)

SCR36=int(input("enter the 21SCR36 marks :"))
sub7=marks_and_credits(SCR36,1)

CIP37=int(input("enter the 21CIP37 marks :"))
sub8=marks_and_credits(CIP37,1)

total_sgpa=(sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8)/18
print("congraluation!!!!")
print("SGPA : ",total_sgpa)