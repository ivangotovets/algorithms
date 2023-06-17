"""
Напишите декоратор answer, который преобразует функцию, принимающую
неограниченное число позиционных и именованных параметров, а возвращает её
результат с припиской "Результат функции: <значение>".
"""


def answer(function):
    def wrapped(*args, **kwargs):
        fn = function(*args, **kwargs)
        return f'Результат функции: {fn}'
    return wrapped


@answer
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
