import time


def fib(limit, get_time=False, shorten_number=False):
    i = 1
    a, b = 1, 2
    if limit == 1 or limit == 0:
        return 1
    seconds = time.time()
    while i < limit - 1:
        a, b = b, a + b
        i += 1
    if shorten_number and len(str(b)) > 6:
        b = f'{int(str(b)[:2])} × 10^{len(str(b)) - 2}'
    if get_time:
        return b, time.time() - seconds
    return b


def fib_recursion(n):
    if n == 0 or n == 1:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


print(fib(10000, get_time=True, shorten_number=True))
print(fib_recursion(10))