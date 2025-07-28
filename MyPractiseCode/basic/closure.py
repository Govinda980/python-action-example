def outer_func(x):
    def inner_func():
        return x + 1

    return inner_func


closure1 = outer_func(5)
closure2 = outer_func(10)

print(closure1() + closure2())


def outer_function(x):
    def inner_function(y):
        return x + 1 + y

    return inner_function


closure = outer_function(5)
result = closure(8)
print("res", result)
