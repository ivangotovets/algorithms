"""
Напишите программу, которая сокращает длинные заголовки до требуемой длины и
завершает их многоточием ... при необходимости.

Формат ввода
Вводится натуральное число
L — необходимая длина заголовка.
Вводится натуральное число
N — количество заголовков, которые требуется сократить.
В каждой из последующих
N строк записано по одному заголовку.

Формат вывода
Сокращённые заголовки.

Примечание
Многоточие учитывается при подсчёте длины заголовка.
25 3 Начался саммит по глобальному потеплению Завтра Новый год!
Python и Java конкурируют за звание самого популярного языка программирования
"""
leng = int(input('Длина зоголовка\n'))
num = int(input('Число заголовков\n'))
list_txt = []
for i in range(1, num+1):
    list_txt.append(input())

for sent in list_txt:
    if len(sent) > leng:
        print(sent[:leng-3] + "...")
