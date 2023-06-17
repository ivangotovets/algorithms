"""
Напишите lambda выражение для фильтрации чисел с чётной суммой цифр.
print(*filter(<ваше выражение>, (1, 2, 3, 4, 5)))
Вывод
2 4
"""
data = (32, 64, 128, 256, 512)
print(*filter(lambda x: not sum(map(int, str(x))) % 2, data))
