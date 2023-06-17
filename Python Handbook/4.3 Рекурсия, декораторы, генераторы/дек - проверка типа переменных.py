"""
Разработайте декоратор same_type, который производит проверку переменного
количества позиционных параметров. В случае получения не одинаковых типов
выводит сообщение "Обнаружены различные типы данных" и прерывает выполнение функции.

@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')

Обнаружены различные типы данных
Fail
Обнаружены различные типы данных
Fail
2
"""


def same_type(function):
    def wrapper(*args):
        if len(args) >= 2:
            for i in range(len(args)-1):
                if type(args[i]) != type(args[i+1]):
                    print('Обнаружены различные типы данных')
                    return False
                break
        return function(*args)

    return wrapper


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
print(False or 'Fail')
