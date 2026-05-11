import math


def get_xc(u, i, f):
    u = float(u)
    i = float(i)
    f = float(f)
    return f'X = {(u / (i * 10 ** -6)) / 1000} kiloohm\nC = {((i * 10 ** -6) / (2 * math.pi * f * u)) * 10 ** 9} nF\n'


while True:
    print(get_xc(input("U [V]: "), input("I [microA]: "), input("f [Hz]: ")))