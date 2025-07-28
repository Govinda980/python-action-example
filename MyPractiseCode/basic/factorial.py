def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


# Example usage:
n = 5
print(f"The factorial of {n} is {factorial(n)}")
