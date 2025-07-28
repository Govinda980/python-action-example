class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"my name is {self.name} and age is {self.age}")


class Student(Person):
    def __init__(self, name, age, grade, section):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.grade = grade
        self.section = section

    def display(self):
        print(self.name, self.age, self.grade, self.section)


ob = Student("Riyansh", 1, 'A', 'A')
ob.display()
