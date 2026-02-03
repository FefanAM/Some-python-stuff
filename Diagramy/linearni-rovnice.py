def solve_linear(a, b):
    if a == 0 and b == 0:
        return "Rovnice ma nekonecne reseni"
    if a == 0 and b != 0:
        return "Rovnice nema reseni"
    return -b / a

print(solve_linear(int(input('Zadej koeficient a:')), int(input('Zadej koeficient b:'))))