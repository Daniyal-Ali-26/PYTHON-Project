ch='y'
total=0
print("            TOTAL  BILL               ") 
while ch=='y' or ch=='Y':
   
    item = int(input("Enter the ITEM Price :"))
    total=total+item
    
    ch = input("If you want to continue press Y \n for stop press T :")
    print("___________________________________________________________________")
print(f"Total Amount=",total)