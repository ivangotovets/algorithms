"""
Частотный анализ — подсчёт, какие символы чаще всего встречаются в тексте.
Это важнейший инструмент взлома многих классических шифров — от шифра Цезаря и
до шифровальной машины «Энигма». Выполним простой частотный анализ: выясним,
какой символ встречается в тексте чаще всего.

Формат ввода
Вводятся строки, пока не будет введена строка «ФИНИШ».

Формат вывода
Выводится один символ в нижнем регистре — наиболее часто встречающийся во
введённой строке.

Ввод
Баобаб
Белка
Бобы
ФИНИШ
Вывод
б
"""
accum = []
elem = ''
while elem != 'Stop':
    elem = input()
    accum += list(elem.lower())

letters = set(accum)

max_letter = ''
max_count = 0
for letter in letters:
    count = accum.count(letter)
    if count > max_count:
        max_count = count
        max_letter = letter

print(max_letter)

