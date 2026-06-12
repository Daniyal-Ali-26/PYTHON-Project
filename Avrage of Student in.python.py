class Student:
    def input(self):
        self.name=input("Enter the Name :")
        self.roll=int(input("Enter the ROLL Number :"))
        print()
        self.m1=float(input("Enter the Physics Marks :"))
        self.m2=float(input("Enter the Chemistry Marks :"))
        self.m3=float(input("Enter the Maths Marks :"))

    def dispaly(self):
        print("____________Students Details__________________")
        print(f"Name :{self.name}")
        print(f"Roll Number :{self.roll}") 
        print()   
        print(f"Physics Marks :{self.m1}")
        print(f"Chemistry Marks :{self.m2}")
        print(f"Maths Marks :{self.m3}")

    def Avrage(self):
        self.total=self.m1+self.m2+self.m3
        self.Avrage = (self.total/300)*100
        print()
        print(f"Parcentage of Student :{self.Avrage}")
        print("___________________________________________________")

        if self.Avrage > 36 and self.m1 >36 and self.m2 > 36 and self.m3 > 36 :
            print("Student is PASS")   
        else:
            print("Student is FAIL")    
    print("_______________________________________________________________")
    print()       
    print("===================================================================")

ch = 'y'
while ch == 'y' or ch == 'Y':
  s = Student()
  s.input()
  s.dispaly()  
  s.Avrage()  
    
  
 
  ch = input("If you want to continue press Y, for Stop press T : ")   
  print("==============================================================")


       