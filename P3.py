class Student:
    def __init__(self):
        self.__name = "PythonLobby.com"

    def get_name(self):
        return self.__name

    def __fun_name(self):
        return "Method Here"

    def get_fun_name(self):
        return self.__fun_name()


class Subject(Student):
    pass


obj = Student()
obj1 = Subject()

# Accessing using object reference of Student class
print(obj.get_name())      # PythonLobby.com
print(obj.get_fun_name())  # Method Here

# Accessing using object reference of Subject class
print(obj1.get_name())     # PythonLobby.com
print(obj1.get_fun_name()) # Method Here
