class Student:
    def __init__(self, age, name):
        self.__age = age

    def __funName(self):
        self.y = 34
        print(self.y)

class Subject(Student):
    pass

# Provide age and name arguments when creating the instance of Student
obj = Student(21, "pythonlobby")
obj1 = Subject()

# Calling by object reference of class Student
print(obj._Student__age)
print(obj._Student__funName())

# Since Subject does not have __age, it throws an AttributeError
# print(obj1._Student__age)

# But we can still call the method from the parent class
print(obj1._Student__funName())


