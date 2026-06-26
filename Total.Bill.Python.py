ch='y'
total=0
print("            TOTAL  BILL               ") 
while ch=='y' or ch=='Y':
        while True:
            try:
                item = int(input("Enter the ITEM Price :"))
                break
            except ValueError:
                print("Error, (Invalid Number)  please Re-enter the price!")
                continue
            
        total=total+item
        while True:
           try:
               ch = input("If you want to continue press Y \n for stop press T :")  
               if ch.isdigit():
                    raise ValueError("Error, (Invalid Number)  please Re-enter the Option!")
               
               break
           except ValueError as v:
              print(v) 
print("___________________________________________________________________")
print(f"Total Amount=",total)





