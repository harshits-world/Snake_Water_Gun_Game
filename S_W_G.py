'''      -1 : Snake
          0 : Water
          1 : Gun      '''

import random
Computer=random.choice([-1, 0, 1])                   #For Computer to choose Random 
 
Input=input("Enter Your Choice: ")                   #Taking Input from Player
YouDict={"Snake" : -1 , "Water" : 0 , "Gun" : 1}     #Made a dictionary to keep record to match the Input from User and the Number for the Computer
ReverseDict={-1 : "Snake" , 0 : "Water" , 1 : "Gun"} #Made a dictionary for using while printing the choice of Both Computer and the Player
You=YouDict[Input]                                   #Taking the integer input by using "Input" and "YouDict"

#By Now , we have only 2 Variables , Computer and You

print(f"You chose {ReverseDict[You]}\nComputer chose {ReverseDict[Computer]}")

if(Computer==You):
    print("It's a Draw")
else:    
    if(Computer==-1 and You==0):
        print("You Lose")
    elif(Computer==-1 and You==1):
        print("You Win")
    elif(Computer==0 and You==-1):
        print("You Win")
    elif(Computer==0 and You==1):
        print("You Lose")
    elif(Computer==1 and You==-1):
        print("You Lose")
    elif(Computer==1 and You==0):
        print("You Win")
    else:
        print("Something Went Wrong")