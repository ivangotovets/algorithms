"""
Напишите lambda выражение для сортировки списка слов сначала по длине,
а затем по алфавиту без учёта регистра.

Ввод
string = 'мама мыла раму' print(sorted(string.split(), key=<ваше выражение>))
Вывод
['мама', 'мыла', 'раму']

Ввод
string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=<ваше выражение>))
Вывод
['во', 'Python', 'многих', 'Яндекс', 'проектах', 'использу']
"""

string = 'Яндекс использefddd Python во многих проектах'
print(sorted(string.split(), key=lambda line: (len(line), str.lower)))