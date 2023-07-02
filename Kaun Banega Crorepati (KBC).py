print("welcome to Tech Quiz")
name=input("enter your name:")

#list to store the question
question=["solve 2*4*3 a)24 b)35 c)86 d)42",
          "which of the following is odd number a)2 b)88 c)51 d)122",
          "solve 2*8+3/4 a)61.00 b)16.00 c)16.75 d)61,75"
          ]

#list to store the answer
answer=["a",
        "c",
        "c"
        ]
#print the question and take the answer
def print_question():
    prize=0 
    for i in range(len(question)):
        print(i+1,":",question[i])
        ans=input("enter the answer:")
        gift=check_answer(ans,i)
        if gift==1:
            prize=prize+1000
            print("Congratulations!",name,"You earned $", prize)        

#check the answer correct or not
def check_answer(ans,i):
    if answer[i]==ans:
        print("correct answer!")
        return 1
    else:
        print("incorrect answer!")
        return False
    
    
#main function
print_question()

