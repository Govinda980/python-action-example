mul = lambda a, b: a * b
print(mul(2, 3))


def calculate(n):
    return lambda a: a * n


c = calculate(6)
print(c(2))
