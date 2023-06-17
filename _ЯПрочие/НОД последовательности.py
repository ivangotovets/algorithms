"""
Наибольший общий делитель последовательности
"""


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def gcd_seq(*args):
    if len(args) == 2:
        return gcd(*args)
    return gcd_seq(*args[1:])


numbers = '2 6 14 20'


list_num = [int(x) for x in numbers.split(' ')]
print(gcd_seq(*list_num))
