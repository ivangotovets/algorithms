"""
Разработайте функцию modern_print, которая принимает строку и выводит её,
если она не была выведена ранее.
Декоратор хранитель Cache
"""

def cache(func):
    _cache = []
    def wrapper(*args):
        if args not in _cache:
            _cache.append(args)
            return func(*args)
    return wrapper

@cache
def modern_print(line):
    print(line)


modern_print("Ало!")
modern_print("Ало!")
modern_print("Я тебя не слышу")
modern_print("Ало!")
modern_print("Ало!")
modern_print("Позвони когда сможешь")
modern_print("Позвони когда сможешь")
modern_print("Я тебя не слышу")
