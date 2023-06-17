"""
Формат ввода
Вводится натуральное число
N
N — количество чисел.
В каждой из последующих
N
N строк записано по одному числу.
В последней строке записано натуральное число
P
P — степень, в которую требуется возвести числа.

Формат вывода
Последовательность чисел, являющихся ответом.
"""
n = int(input('No digits\n'))
list_num = []
for i in range(0, n):
    list_num.append(int(input()))
p = int(input('Exponent\n'))

result = [x ** p for x in list_num]
for num in result:
    print(num)

