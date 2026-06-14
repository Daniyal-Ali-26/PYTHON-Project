class billty:
    def info(self):
        self.name = input("Enter the coustemer name :")
        self.place = input("Enter the place name :")
        self.LRNum = int(input("Enter the LR Number :"))
        self.lot = int(input("Enter the LOT :"))
        self.price = float(input("Enter the Price :"))

    def display(self):
        print()
        print("============Ditails===============")
        print(f"Coustemer Name :{self.name}")
        print(f"Place :{self.place}")
        print(f"LR Number :{self.LRNum}")
        print(f"LOT :{self.lot}")
        print(f"Price :{self.price}")    

ch = 'y'
while(ch == 'y' or ch == "Y"):
  b = billty()
  b.info()
  b.display()
  ch = input("If you want to stop press Y  \n for stop press T :")
  print("=====================================================")