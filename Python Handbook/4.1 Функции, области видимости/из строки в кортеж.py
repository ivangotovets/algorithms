"""
Разработайте функцию split_numbers, которая принимает строку целых чисел,
разделённых пробелами, и возвращает кортеж из этих чисел.
result = split_numbers("1 2 3 4 5")
result = (1, 2, 3, 4, 5)
"""

def split_numbers(numbers):
    acc = [int(x) for x in numbers.split(" ")]
    return tuple(acc)

print(split_numbers("1 2 3 4 5"))

