"""
Вашему решению будет предоставлена строка text.
Напишите выражение для генерации словаря, который содержит информацию о
частоте употребления букв в заданной строке.
При анализе не учитывайте регистр, а ключами словаря сделайте использованные
в строке буквы в нижнем регистре.

Ввод
text = 'Мама мыла раму!'
Вывод
{'а': 4, 'л': 1, 'м': 4, 'р': 1, 'у': 1, 'ы': 1}
"""
import collections

text = 'Мама мыла раму!'
d = {x: text.count(x) for x in set(text.casefold()) if x.isalpha()}
print(sorted(d.items()))
res = collections.OrderedDict(sorted(d.items()))
print(res)
