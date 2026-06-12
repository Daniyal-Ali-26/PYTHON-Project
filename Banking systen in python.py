class BankAccount:
    
    def input(self):
        self.name = input("Enter the Name :")
        self.Ac = int(input("Enter the Number :"))
        self.balance = int(input("Enter the Current Balance :"))
        
    
    def Show(self): 
        print("_________________________DETAILS____________________________")   
        print(f"Name :{self.name}")
        print(f"Accont Number :{self.Ac}")
        print(f"Current Balance :{self.balance}")
        print("_______________________________________________")

    def WithDraw(self):
        amount = float(input("Enter the Withdraw Amount :"))
        self.balance=self.balance - amount
        print(f"The Remening Balance :{self.balance}") 

    def Deposite(self):
        amount = float(input("Enter the Deposite Amount :"))
        self.balance=self.balance + amount
        print(f"The Updated Balance :{self.balance}")        
print("==========================BANKING SYSTEM===========================")
ch = 'y'
while ch == 'y' or ch == 'Y':
  b = BankAccount()
  b.input()
  b.Show()
  print("For Withdraw Press 1")
  print("For Deposite Press 2")
  choise = int(input("Enter the Choise :"))
  match choise:
    case 1:
        b.WithDraw()
    case 2:
        b.Deposite()
    case _:
        print("Please Choose the Correct Number")  
  print("______________________________________________________________")      
  ch = input("If you want to continue press Y, for Stop press T : ")         
print("=================================================================") 
print("THANK YOU FOR USING THIS SYSTE!")

