class Father:
    def __init__(self, title):
        self.title = title

    def display(self):
        print(self.title)


class Mother:
    def __init__(self, address):
        self.address = address

    def address_show(self):
        print(self.address)


class Child(Father, Mother):
    def __init__(self, name, title, address):
        self.name = name
        Father.__init__(self, title)
        Mother.__init__(self, address)

    def display_name_title(self):
        print(self.name, self.title, self.address)


ob = Child('Govinda', "Kumar", "Bhavnagar")
ob.display_name_title()


# class A:
#     def method_A(self):
#         print("method A")
#
#     def test(self):
#         print("Hi A")
#
#
# class B:
#     def method_B(self):
#         print("method B")
#
#     def test(self):
#         print("Hi B")
#
#
# class C(A, B):
#     def method_C(self):
#         print("Method C")
#
#
# ob = C()
# ob.method_A()
# ob.method_B()
# ob.test()