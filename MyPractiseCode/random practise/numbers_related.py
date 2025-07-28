"""
Convert 123 to base 5
123 ÷ 5 = 24 (quotient), remainder = 3
24 ÷ 5 = 4 (quotient), remainder = 4
4 ÷ 5 = 0 (quotient), remainder = 4
we get the base 5 number 443
"""


# import pdb

def convert_number_to_many_form():
    num = 123
    base = 10
    rem_storage = []
    rem_num = []
    while num > 0:
        rem = num % base
        num = num // base
        # pdb.set_trace()
        rem_storage.append(rem)
    rem_storage.reverse()
    for i in rem_storage:
        rem_num.append(str(i))
    base_con = ''.join(rem_num)
    print(base_con)


def reverse_num():
    num = 123
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    print(rev)


def digit_count_in_number():
    num = 1234
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
    print("digit count", count)


def digit_sum():
    num = 1234
    reserve = num
    result = 0
    while num > 0:
        rem = num % 10
        result += rem
        num = num // 10
    print(f"digit sum of {reserve}---->", result)


def multiplication_table():
    num = 6
    times = 10
    for i in range(1, times + 1):
        print(f"{num}*{i} is {num * i}")


def prime_number_check(num):
    count = 0
    for i in range(2, num // 2):
        if num % i == 0:
            count += 1
    if count == 0:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not prime number")


def prime_num_range():
    for i in range(2, 100):
        prime_number_check(i)


def str_test():
    tt = str if str == 'Hello World!' else 'Test'
    print(tt)
    num = int if int == 10 else 1
    print(num)


if __name__ == '__main__':
    # convert_number_to_many_form()
    # str_test()
    # reverse_num()
    # digit_count_in_number()
    # digit_sum()
    # multiplication_table()
    # prime_number_check()
    prime_num_range()
 

