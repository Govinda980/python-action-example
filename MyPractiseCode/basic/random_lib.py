import random

print(random.random())  # give float in range 0 to 1
print(random.uniform(1, 100))  # any one float in range 1 to 100
print(random.randint(1, 100))  # any one integer from 1 to 100
print(random.randrange(0, 100, 2))  # any one 1 to 100 even num
print(random.sample(range(1, 100), 3))  # return 3 random number
print(list(range(1, 5)))

li = [1, 2]

l2 = li
l2.append(7)
l3 = li.copy()
print(l2 is li)


temp = 10  # global-scope variable


def func():
    temp = 20  # local-scope variable
    print(temp)


print(temp)  # output => 10
func()  # output => 20
print(temp)  # output => 10
