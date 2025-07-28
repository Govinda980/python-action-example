class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

    def disp(self):
        print("c", self.__c)


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        # print(self.__c) #this will throe error


# Driver code
obj1 = Derived()
obj1.disp()  # this will execute because it belongs to the class
# print(obj1.__c) # throw error, directly can'not access private variable
