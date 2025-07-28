def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


total = 0
for i in range(2, 20):
    if is_prime_number(i):
        print(i)
        total += i

print("total sum of prime number", total)
