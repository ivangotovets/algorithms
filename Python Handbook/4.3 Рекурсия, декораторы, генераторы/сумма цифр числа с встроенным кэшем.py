"""
Напишите функцию recursive_digit_sum, которая находит сумму всех цифр натурального числа.
result = recursive_digit_sum(123)
result = 6
"""
from functools import lru_cache

@lru_cache(maxsize=1000)
def recursive_sum(seq):
    if seq % 10 == 0:
        return 0
    return seq % 10 + recursive_sum(seq // 10)


print(recursive_sum(7321346))