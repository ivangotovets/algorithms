"""
Напишите функцию gcd, которая вычисляет наибольший общий делитель последовательности чисел.
Параметрами функции выступают натуральные числа в произвольном количестве, но не менее одного.
Ввод
result = gcd(3)
Вывод
result = 3

Ввод
result = gcd(36, 48, 156, 100500)
Вывод
result = 12
"""


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def seq_gcd(*args):
    if len(args) == 2:
        return gcd(*args)
    return seq_gcd(*args[1:])

seq = [15, 35, 100]
print(seq_gcd(*seq))

