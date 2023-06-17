"""
Fibonacci
функция-генератор
print(*fibonacci(5))
0 1 1 2 3

print(*fibonacci(10), sep=', ')
0, 1, 1, 2, 3, 5, 8, 13, 21, 34

"""
from functools import lru_cache

#обычная рекурсивная функция
@lru_cache(maxsize=1000)
def fib(n):
    if n in (0, 1):
        return 1
    return fib(n-1) + fib(n-2)

#функция-генератор
def fib_2(n):
    f, f1 = 0, 1
    for i in range(0, n):
        yield f
        f, f1 = f + f1, f


print(*fib_2(5), sep=",")