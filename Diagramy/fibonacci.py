import time
from textwrap import shorten


def fib(limit, get_time=False, shorten_number=False, print_num=True):
    i = 1
    a, b = 1, 2
    if limit == 1 or limit == 0:
        return 1
    seconds = time.time()
    while i < limit - 1:
        a, b = b, a + b
        i += 1
    if not print_num:
        return f'Process took {time.time() - seconds} seconds to compute {limit} numbers.'
    if shorten_number and i > 20:
        b = f'{int(str(b)[:2])} × 10^{len(str(b)) - 2}'
    if get_time:
        return b, time.time() - seconds
    return b


def fib_recursion(n):
    if n == 0 or n == 1:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


print(fib(1000000, print_num=False))
print(fib_recursion(10))
