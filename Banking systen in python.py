class BankAccount:
    
    def input(self):
        
        self.name = input("Enter the Name :")
        if self.name.isdigit():
             raise ValueError("Numeric Words is not allowed in name...")
       
         
        try:
          self.Ac = int(input("Enter the Number :"))
          self.balance = int(input("Enter the Current Balance :"))
        except ValueError:
           print("Please Enter a Numeric Values...")
           return False
    
    def Show(self): 
        print("_________________________DETAILS____________________________")   
        print(f"Name :{self.name}")
        print(f"Accont Number :{self.Ac}")
        print(f"Current Balance :{self.balance}")
        print("_______________________________________________")

    def WithDraw(self):
       try: 
         amount = float(input("Enter the Withdraw Amount :"))
         if amount>self.balance:
            raise ValueError("Insufficient Balance!")
         self.balance=self.balance - amount
         print(f"The Remening Balance :{self.balance}") 
       except ValueError as v: 
          print(v)
           

    def Deposite(self):
      try:  
        amount = float(input("Enter the Deposite Amount :"))
        if amount<=0:
           raise ValueError("Deposite Amount is must be Positive")
        self.balance=self.balance + amount
        print(f"The Updated Balance :{self.balance}")  
      except ValueError as v:
         print(v)        
print("==========================BANKING SYSTEM===========================")
ch = 'y'
while ch == 'y' or ch == 'Y':
  b = BankAccount()
  if b.input() != False:
   b.Show()
  print("For Withdraw Press 1")
  print("For Deposite Press 2")
  try:
    choise = int(input("Enter the Choise :"))
  except ValueError:
    print("Please enter 1 or 2")
    continue
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

