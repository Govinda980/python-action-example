class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        self.name = "Govinda You Are Looser"

    @classmethod
    def total_instances(cls):
        return f"Total instances created: {cls.count}"


MyClass()
MyClass()
print(MyClass.total_instances())
