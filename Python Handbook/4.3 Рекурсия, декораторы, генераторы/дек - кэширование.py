"""
Кэширование внутри декоратора
"""

from functools import wraps


def cache3(func):
    count = {0:0}
    cache = {0:0}
    @wraps(func)
    def wrapper():
        if count[0] % 3 == 0:
            cache[0] = func()
            count[0] += 1
            return cache[0]
        count[0] += 1
        return cache[0]
    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1