"""
Напишите функцию is_prime, которая принимает натуральное число, а возвращает
булево значение: True — если переданное число простое, а иначе — False.
обычный и решето эратосфена
"""
from math import sqrt


def is_prime_simple(x):
    for i in range(2, int(round(sqrt(x))+1)):
        if x % i == 0:
            return False
        return True




print(is_prime_simple(1001457))