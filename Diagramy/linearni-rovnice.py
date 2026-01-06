def solve_linear(a, b):
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        return "Rovnice ma nekonecne reseni"
    if a == 0 and b != 0:
        return "Rovnice nema reseni"
    return -b / a

print(solve_linear(input('Zadej koeficient a:'), input('Zadej koeficient b:')))