def reverse_number(n):
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    print(rev)


def reverse_str(s):
    rev_str = s[::-1]
    # print(rev_str)
    end = len(s) - 1
    st_r = ''
    for i in range(end, -1, -1):
        st_r += s[i]
    print(st_r)


def palindrome(s):
    palin = 'yes' if s == s[::-1] else 'no'
    # print(palin)
    mid = int(len(s) / 2)
    flag = 0
    for i in range(mid):
        if s[i].lower() != s[len(s) - 1 - i].lower():
            flag = 0
        else:
            flag = 1
    if flag == 1:
        print("Yes")
    else:
        print("No")


# 1 + 125 + 27 = 153 Armstrong

def armstrome_number(n):
    sum = 0
    reserve = n
    while n > 0:
        rem = n % 10
        print("rem", rem)
        sum += pow(rem, 3)
        n = n // 10
    print(sum)
    if sum == reserve:
        print(f"Yes {reserve} is Armstrong number")
    else:
        print(f"{reserve} is not Armstrong number")


# 2, 3, 5, 7, 13,
def is_prime_number(n):
    c = 0
    for i in range(2, n // 2):
        if n % i == 0:
            c = c + 1

    if c == 0:
        print("Prime")
    else:
        print("No")


def prime_range(n):
    prim_num = []
    for i in range(2, n):
        c = 0
        for j in range(2, i):
            if i % j == 0:
                c = c + 1
        if c == 0:
            prim_num.append(i)
    print(prim_num)


# 0, 1, 1, 2, 3, 5, 8 ……
def focaccia_series(n):
    a = 0
    b = 1
    for i in range(2, n):
        print(b)
        c = a + b
        a = b
        b = c



if __name__ == '__main__':
    # reverse_number(123)
    # reverse_str('Govinda')
    # palindrome('level')
    # armstrome_number(153)
    # is_prime_number(15)
    # prime_range(10)
    focaccia_series(10)
