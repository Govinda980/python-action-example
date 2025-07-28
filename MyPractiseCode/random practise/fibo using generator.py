import time


def febo_fun_gen():
    a = 0
    b = 1
    n = 10
    print(a)
    for i in range(2, n):
        yield b
        c = a + b
        a = b
        b = c


for item in febo_fun_gen():
    print(item)
