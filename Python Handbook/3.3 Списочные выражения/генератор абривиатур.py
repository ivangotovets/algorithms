"""
Вашему решению предоставлена строка string.
Напишите выражение для генерации строки, представляющей собой аббревиатуру заданной.

Ввод
string = 'Российская Федерация'
Вывод
'РФ'
"""
string = 'Российская Федерация Ниибацо'
print(''.join(x for x in string if x.isupper()))
