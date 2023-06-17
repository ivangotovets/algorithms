"""
Напишите функцию recursive_sum, которая находит сумму всех позиционных аргументов.

result = recursive_sum(1, 2, 3)
# Вызов recursive_sum(1, 2, 3)
# Вызов recursive_sum(1, 2)
# Вызов recursive_sum(1)
# Вызов recursive_sum()
result = 6
"""
from functools import lru_cache


@lru_cache(maxsize=1000)
def recursive_sum(*args):
    if len(args) == 0:
        return 0
    return args[-1] + recursive_sum(*args[:-1])


print(recursive_sum(1, 3, 4, 6))

