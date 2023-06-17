"""
Весьма часто, данные, которые мы получаем из различных источников, не
удовлетворяют нашим пожеланиям. Одна из частых проблем – излишняя вложенность списков.

Напишите функцию make_linear, которая принимает список списков и возвращает
его "выпрямленное" представление.
result = make_linear([1, 2, [3]])
# Вызов make_linear([1, 2, [3]])
# Вызов make_linear([3])
result = [1, 2, 3]
result = make_linear([1, [2, [3, 4]], 5, 6])
# Вызов make_linear([1, [2, [3, 4]], 5, 6])
# Вызов make_linear([2, [3, 4]])
# Вызов make_linear([3, 4])
result = [1, 2, 3, 4, 5, 6]
"""


from collections import abc


def flatten(iterable):
    for item in iterable:
        if isinstance(item, (str, bytes)):
            yield item
        elif isinstance(item, abc.Sequence):
            yield from flatten(item)
        else:
            yield item




print(list(flatten(([1, 2, [3]]))))
