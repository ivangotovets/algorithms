# регистратор
register = {}
def registrator(name):
    def inner(func):
        register[name] = func
        return func
    return inner


# cache
def cache(func):
    _cache = {}

    def inner(*args):
        result = _cache.get(args)
        if result is not None:
            return result
        else:
            result = func(*args)
            _cache[args] = result
            return result
    return inner