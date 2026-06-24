class BookManagement:
    def __init__(self):
        self.books=[]

    def addBook(self):
       print("__________________________________________________")
       while True: 
           
            try:
                 id = int(input("Enter Book ID: "))
                 
                 if any(book["id"] == id for book in self.books):
                         print("This ID already Exists")
                         continue
                 break
            except ValueError:
                 print("Please enter a valid numeric ID!")
                 continue
            
       while True:
          
          try:
             name = input("Enter The Book Name :")
             if name.isdigit():
                 raise ValueError("Error, Numeric From is Not Allowd in Name!")
             break
          except ValueError as e:
            print(e)
               
       book = {    "id" : id ,  
                "Name" : name   
               }      
       self.books.append(book)   
       print("Book Added Successfully!")


    def deleteBook(self):
        while True: 
            
            try:
                 id = int(input("Enter Book ID: "))
                 break
            except ValueError:
                 print("Please enter a valid numeric ID!")
                 continue
        for book in self.books:
            if book["id"] == id:
                self.books.remove(book)              
                print("Book Removed Successfully!")
                return
        print("Book Not Found!")

    def BookUpdate(self):
       while True: 
            
            try:
                 id = int(input("Enter Book ID: "))
                 break
            except ValueError:
                 print("Please enter a valid numeric ID!")
                 continue
       for book in self.books:
            if book["id"] == id:
               while True:   
                  try:
                     newName = input("Enter the New Name for Book :")
                     if newName.isdigit():
                            raise ValueError("Error, Numeric From is Not Allowd in Name!")
                     
                     
                     break  
                  except ValueError as e:
                         print(e)
               book["Name"] = newName
               print("Book Name Updated Successfully!")
               return
                  
            
       print("Book Not Found!")
    def SearchBook(self):
      while True: 
          
          try:
              id = int(input("Enter Book ID: "))
              break
          except ValueError:
              print("Please enter a valid numeric ID!")
              continue

      for book in self.books:
          if book["id"] == id:
              print("Book Found!")
              print(f"Book ID: {book['id']} | Book Name: {book['Name']}")
              return

      print("Book Not Found!") 
    
    def viewBooks(self):
        if len(self.books) == 0:
            print("No Books Available!")
            return
        print("\n Books Are Available!")   
        for book in self.books:
           print(f"Book ID: {book['id']} | Book Name: {book['Name']}") 



Library = BookManagement()
while True:
   print("================Book Management System=============")        
   print("For ADD BOOK Press 1")    
   print("For DELETE BOOK Press 2")
   print("For UPDATE BOOK Press 3")
   print("For VIEW BOOK Press 4")
   print("For Search Press 5")
   print("FOR EXIT Press 6")
   print("__________________________________________")

   while True: 
      try: 
         choise = int(input("Enter the Choice :"))
         break
      except ValueError:
          print("Plrase Enter a Numeric Choice!")
          continue

   match choise:
       case 1:
           Library.addBook()
       case 2:
           Library.deleteBook()
       case 3:
           Library.BookUpdate()
       case 4:
           Library.viewBooks()  
       case 5:
           Library.SearchBook()     
       case 6:
           print("Thank you!")
           break         
       case _:
           print("You Entered Invalid Choice!")
    
              
           




