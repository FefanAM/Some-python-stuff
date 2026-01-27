import time


def eratosthenes_sieve(n):
    is_prime = [True] * (n // 2 + 1)
    is_prime[0] = False

    p = 3
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n // 2 + 1, p):
                is_prime[i] = False
        p += 1

    primes = [2]
    for p in range(len(is_prime)):
        if is_prime[p]:
            primes.append(p * 2 + 1)
    return primes


def sito(n):
    number_row = [*range(1, n + 1, 2)]

    for num in range(2, int(n ** 0.5) + 1):
        if num not in number_row:
            continue
        else:
            for i in range(num * num, n + 1, num * 2):
                if i in number_row:
                    number_row.remove(i)

    return number_row


print(eratosthenes_sieve(100000))
