a = [1, 2, 3]
b = a
a = a + [4, 5]
print(b)  # The concatenation creates a new list, and b still refers to      the original list.

x = [1, 2, 3]
y = x
x = x + [4, 5]
print(y)
# The += operator modifies the list in-place, and y reflects this change.


c = [1, 2, 3]
d = c[:]
d[0] = 10
print(c)


def modify_list(my_list):
    my_list = [0, 1, 2]


original_list = [1, 2, 3]
modify_list(original_list)
print("original", original_list)


def some_function(*args, **kwargs):
    return args, kwargs


result = some_function(1, 2, a=3, b=4)
print(result)

x = [1, 2, 3]
y = x + [4, 5]
z = x.extend([4, 5])
print(x, y, z)

my_list = [1, 2, 3, 4]
result = [x if x % 2 == 0 else -x for x in my_list]
print(result)

x = 10


def multiply_by_two():
    global x
    x *= 2


multiply_by_two()
print(x)


def mystery_function(x):
    return x if x > 0 else mystery_function(-x)


result = mystery_function(-5)
print(result)

# class CustomError(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
# raise CustomError("An example custom error.")

string1 = "Python"
string2 = "Python"
result = string1 is string2
print(result)  # True String interning in Python makes identical string literals refer to the same memory location.


def my_generator():
    for i in range(5):
        yield i * 2


result = list(my_generator())
print(result)


def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


@my_decorator
def my_function(s):
    return s + 1


result = my_function(5)
print(result)


class MyClass:
    x = 10


obj1 = MyClass()
obj2 = MyClass()
obj1.x += 5
result = obj2.x
print(result)


class CustomClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


obj = CustomClass(42)
result = obj.get_value()
print(result)


class CustomClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


obj1 = CustomClass(10)
obj2 = CustomClass(10)
result = obj1 == obj2
print(result)  # true The custom __eq__ method is defined to compare the value attribute of the objects.
