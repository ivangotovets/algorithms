"""
Таблица умножения 2.0
Вашему решению будет предоставлена единственная переменная n — необходимый размер таблицы умножения.
Напишите списочное выражения для генерации таблицы умножения.

Ввод
n = 3
Вывод
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
"""
n = 3
print([[x*i for x in range(1, n+1)] for i in range(1, n+1)])
