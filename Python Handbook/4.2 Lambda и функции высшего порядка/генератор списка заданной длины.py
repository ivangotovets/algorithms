"""
Напишите функцию make_list, которая создаёт, заполняет и возвращает список заданного размера.
Параметры функции
length — требуемая длина списка;
value — значение элементов списка (по-умолчанию 0).
Ввод
result = make_list(3)
Вывод
result = [0, 0, 0]
Ввод
result = make_list(5, 1)
Вывод
result = [1, 1, 1, 1, 1]
"""

def make_list(len, val=0):
    res_list = [(lambda x: val)(x) for x in range(1, len+1)]
    return res_list


print(make_list(4))

