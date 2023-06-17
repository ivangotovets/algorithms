def cache(func):
    _acc = {}
    def wrapper(*args):
        if args not in _acc:
            _acc[args] = func(*args)
            print('Запись в кэш')
        return _acc[args]
    return wrapper

inp = list(map(int, input('Числа: ').split()))

@cache
def c_print(seq):
    print(seq)

for x in inp:
    c_print(x)


