import random

# Program to generate a random single digit number

num = random.randint(1, 10)
print(num)

# Generate a Random Number between 0 and 1
num = random.random()
print(num)

# Random floating value
num = random.uniform(1, 10)
print(num)

# random 1 odd number number

num = random.randrange(1, 100, 2)
print(num)

# random 1 even number number

num = random.randrange(2, 100, 2)
print(num)

# gen random 2 item in list
list_test = [1, 2, 3, 4, 5]
item = random.sample(list_test, 2)
print(item)

# one item from list
item = random.choice(list_test)
print(item)


# make list item random
random.shuffle(list_test)
print(list_test)

