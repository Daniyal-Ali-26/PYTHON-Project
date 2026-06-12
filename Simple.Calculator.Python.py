def add():
 ch='y'
 while ch == 'y' or ch == 'Y' :
    a = int(input("Enter the Number :"))
    b = int(input("Enter the Number :"))
    sum=a+b
    print(f":{sum}")
   
    ch = input("If you want to add (y/n)")
    print("____________________________________________________________________")


def sub():
 ch='y'
 while ch == 'y' or ch == 'Y' :
    a = int(input("Enter the Number :"))
    b = int(input("Enter the Number :"))
    sum=a-b
    print(f":{sum}")
   
    ch = input("If you want to add (y/n)")
    print("____________________________________________________________________")
   

def multi():
 ch='y'
 while ch == 'y' or ch == 'Y' :
    a = int(input("Enter the Number :"))
    b = int(input("Enter the Number :"))
    sum=a*b
    print(f":{sum}")
   
    ch = input("If you want to add (y/n)")
    print("____________________________________________________________________")
      

def division():
 ch='y'
 while ch == 'y' or ch == 'Y' :
    a = int(input("Enter the Number :"))
    b = int(input("Enter the Number :"))
    sum=a/b
    print(f":{sum}")
   
    ch = input("If you want to add (y/n)")
    print("____________________________________________________________________")
         

print("       SIMPLE  CALCULATOR      ")
print("For Addition Press 1")
print("For Substraction Press 2")
print("For Multiplication Press 3")
print("For Division Press 4")

choise = int(input("Enter the choise :"))
print("__________________________________________________________________")
match choise:
    case 1:
      add()
    case 2:
      sub()
    case 3:
      multi()
    case 4:
      division()
    case _:
      print("Invalid Number please press a correct Number  ")      
print("Thank You For Using ME!")