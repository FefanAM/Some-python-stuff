def eratosthenes_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if p == 2:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
            p += 1
            continue
        if is_prime[p]:
            for i in range(p * p, n + 1, p * 2):
                is_prime[i] = False
        p += 1

    primes = []
    for p in range(n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes


def sito(n):
    number_row = [*range(2, n + 1)]

    for num in range(2, int(n ** 0.5) + 1):
        if num not in number_row:
            continue
        if num == 2:
            for i in range(num * num, n + 1, num):
                if i in number_row:
                    number_row.remove(i)
        else:
             for i in range(num * num, n + 1, num * 2):
                if i in number_row:
                    number_row.remove(i)

    return number_row

print(eratosthenes_sieve(300000000))