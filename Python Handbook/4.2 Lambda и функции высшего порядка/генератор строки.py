"""
Напишите функцию to_string, которая формирует из последовательности данных строку.
Функция должна принимать:
неопределённое количество данных;
необязательный параметр sep (по умолчанию пробел);
необязательный параметр end (по умолчанию \n).
Ввод
data = [7, 3, 1, "hello", (1, 2, 3)] result = to_string(*data, sep=", ", end="!")
Вывод
result = '7, 3, 1, hello, (1, 2, 3)!'
"""


def to_string(*args, sep=' ', end='!'):
    data = tuple(*args)
    result = sep.join(str(x) for x in data)
    result += sep + end
    return result


data = [7, 3, 1, "hello", (1, 2, 3)]


print(to_string(data, sep=","))
