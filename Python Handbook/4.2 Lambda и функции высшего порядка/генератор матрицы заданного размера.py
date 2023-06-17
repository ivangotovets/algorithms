"""
Напишите функцию make_matrix, которая создаёт, заполняет и возвращает матрицу заданного размера.
Параметры функции:
size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы);
value — значение элементов списка (по-умолчанию 0).

Ввод
result = make_matrix(3)
Вывод
result = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
Ввод
result = make_matrix((4, 2), 1)
Вывод
result = [ [1, 1, 1, 1], [1, 1, 1, 1] ]
"""


def make_matrix(*size, value=0):
    if len(size) == 1:
        size += (size[0],)
    f = lambda x: value
    return [[f(x) for x in range(1, size[0]+1)] for y in range(1, size[1]+1)]


print(make_matrix(3))
