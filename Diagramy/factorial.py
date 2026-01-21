def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result = result * num
    return result


print(factorial_rec(8))
print(factorial(0))