import random
'''
1  
0
-1
'''
computer=random.choice([1,0,-1])
youstr=input("Enter the Choise :")
youDict={"s": 1,"w":-1,"g" : 0}
reverseDict = {1 : "Snake" , -1 :"Water", 0 : "Gun"}

you=youDict[youstr]

print(f"You choose {reverseDict[you]} \n Computer choose {reverseDict[computer]}")

if(computer == you):
    print("Its DRAW")
else:
       if(computer == -1 and you == 1):
        print("YOU wIN")  
     
       elif(computer == 1 and you == 0):
           print("YOU LOSE")
       elif(computer == -1 and you == 0):
           print("YOU WIN")
       elif(computer == 0 and you == -1):
           print("YOU WIN")      
       elif(computer == 0 and you == 1):
           print("YOU LOSE")   
       else:
           print("Something went wrong")     