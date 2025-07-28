class MyClass:
    count = 0

    def __init__(self, name):
        self.name = name
        MyClass.count += 1

    def __str__(self):
        return f"Hi I am {self.name}"

    @classmethod
    def total_instances(cls):
        return f"Total instances created: {cls.count}"


obj1 = MyClass("Alice")
obj2 = MyClass("Bob")
print(obj1)

print(MyClass.total_instances())  # Output: Total instances created: 2


