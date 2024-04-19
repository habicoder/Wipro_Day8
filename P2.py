class Student:
     # protected data members
     __name = None
     __roll = None
     __branch = None
     # constructor
     def __init__(self, name, roll, branch):  
          self.__name = name
          self.__roll = roll
          self.__branch = branch
     # protected member function   
     def __displayRollAndBranch(self):
          # accessing protected data members
          print("Roll: ", self.__roll)
          print("Branch: ", self.__branch)

# derived class
class Geek(Student):
       # constructor 
       def __init__(self, name, roll, branch): 
                Student.__init__(self, name, roll, branch) 
       # public member function 
       def displayDetails(self):
                 # accessing protected data members of super class 
                print("Name: ", self.__name) 
                 # accessing protected member functions of super class 
                self.__displayRollAndBranch()
# creating objects of the derived class        
obj = Geek("R2J", 1706256, "Information Technology") 
# calling public member functions of the class
obj.displayDetails()