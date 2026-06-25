class NumberContacts:
    def __init__(self):
        self.contact = []

    # Add Function..............    
    def addContact(self):
        while True:
            try:
                num = int(input("Enter the 10 Digit Mobil Number :"))
                if any(Details["Number"] == num for Details in self.contact):
                    print("Given number is already exists!")
                    continue
                break
            except ValueError:
                print("Error, the number is in Numeric From")
                continue

        while True:
            try:
                name = input("Enter the Name :")
                if name.isdigit():
                    raise ValueError("Error, Please Save the number in Alphabetical Form!")
                break
            except ValueError as v:
                print(v)

        Details = {
            "Number": num,
            "Name": name
        }

        self.contact.append(Details)
        print("Contact Added Successfully!")


    # Delete Contact..............
    def DeleteContact(self):
        while True:
            try:
                num = int(input("Enter the Number :"))
                break
            except ValueError as v:
                print("Error, the number is in Numeric From")

        for Details in self.contact:
            if Details["Number"] == num:
                self.contact.remove(Details)
                print("Number Delete Successfully!")
                break
        else:
            print("Number Not Found!")


    # Search Function...............
    def SearchContact(self):
        while True:
            try:
                num = int(input("Enter the Number :"))
                break
            except ValueError as v:
                print("Error, the number is in Numeric From")

        for Details in self.contact:
            if Details["Number"] == num:
                print(f"Name :{Details['Name']}")
                print(f"Number Found :{Details['Number']}")
                break
        else:
            print("Number Not Found!")


    # Update contact...........................
    def UpdateContact(self):
        while True:
            try:
                num = int(input("Enter the Number :"))
                break
            except ValueError as v:
                print("Error, the number is in Numeric From")

        for Details in self.contact:
            if Details["Number"] == num:
                while True:
                    try:
                        NewName = input("Enter the New Name :")

                        if NewName.isdigit():
                            raise ValueError("Error, please enter the Alphabetical Form!")

                        Details["Name"] = NewName
                        print("Name is Successfully Updated!")
                        break

                    except ValueError as v:
                        print(v)
                break
        else:
            print("Number is Not Found")


    # View Contacts............         
    def ViewContacts(self):
        if len(self.contact) == 0:
            print("No Contact Found in List!")
            return
        else:
            print("\n Contacts Are Available!")

            for Details in self.contact:
                print(f"Name :{Details['Name']}  | Number Found :{Details['Number']}")
       # Main Funtion............................
Numbers = NumberContacts()
while True:
    print("=================Contact Details================")
    print("For Add Contact Press 1")
    print("For Delete Contact Press 2")
    print("For Search Contact Press 3")
    print("For Update Contact Press 4")
    print("For View Contact Press 5")
    print("For Exit Press 6")
    
    while True:
      try:
          choice = int(input("Enter the Choice :"))
          break
      except ValueError:
          print("Error , Invalid Choice....")
          continue
    
    match choice:
        case 1:
            Numbers.addContact()
        case 2:
            Numbers.DeleteContact()
        case 3:
            Numbers.SearchContact()
        case 4:
            Numbers.UpdateContact()   
        case 5:
            Numbers.ViewContacts()
        case 6:
            print("Thank you!")
            break
        case _:
            print("Invalid Choice.....")        


