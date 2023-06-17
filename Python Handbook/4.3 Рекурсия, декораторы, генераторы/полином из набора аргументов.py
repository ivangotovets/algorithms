"""
result = make_equation(3, 2, 1)
# Вызов make_equation(3, 1, 5, 3)
# Вызов make_equation(3, 1, 5)
# Вызов make_equation(3, 1)
# Вызов make_equation(3)
result = '(((3) * x + 1) * x + 5) * x + 3'

"""


def make_equation(*args):
    if len(args) == 1:
        return str(*args)
    return f'({make_equation(*args[:-1])}) * x + {args[-1]}'


print(make_equation(3, 1, 5, 3))
