"""
Наибольший общий делитель последовательности
"""


inp = list(map(int, input('Digits:\n').split()))


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def gcd_seq(*args):
    if len(args) == 2:
        return gcd(*args)
    return gcd(args[0], gcd_seq(*args[1:]))

print(gcd_seq(*inp))
