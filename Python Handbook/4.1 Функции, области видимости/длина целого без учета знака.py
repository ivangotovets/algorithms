"""
Разработайте функцию number_length, которая принимает одно целое число и
возвращает его длину без учёта знака.

result = number_length(-100500)
result = 6
"""


def number_length(x):
    if abs(x) // 10 == 0:
        return 1
    return 1+number_length(x // 10)

print(number_length(-100500))
