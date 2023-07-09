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
CS41=int(input("enter the 21CS41 marks :"))
sub1=marks_and_credits(CS41,3)

CS42=int(input("enter the 21CS42 marks :"))
sub2=marks_and_credits(CS42,3)

CS43=int(input("enter the 21CS43 marks :"))
sub3=marks_and_credits(CS43,3)

CS44=int(input("enter the 21CS44 marks :"))
sub4=marks_and_credits(CS44,3)

BE45=int(input("enter the 21BE45 marks :"))
sub5=marks_and_credits(BE45,2) #credits 2 for biology

CSL46=int(input("enter the 21CSL46 marks :"))
sub6=marks_and_credits(CSL46,1)

KANNADA=int(input("enter the 21KSK47 / 21BSK47  marks :"))
sub7=marks_and_credits(KANNADA,1)

UH49=int(input("enter the 21UH49 marks :"))
sub8=marks_and_credits(UH49,1)

CSL49=int(input("enter the 21CSL49 marks :"))
sub9=marks_and_credits(CSL49,1)

total_sgpa=(sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8+sub9)/18
print("congraluation!!!!")
print("SGPA : ",total_sgpa)