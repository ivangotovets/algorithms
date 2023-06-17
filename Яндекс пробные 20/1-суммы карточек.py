"""
На стол в ряд выложены карточки, на каждой карточке написано натуральное число.
За один ход разрешается взять карточку либо с левого, либо с правого конца ряда.
Всего можно сделать k ходов. Итоговый счет равен сумме чисел на выбранных
карточках. Определите, какой максимальный счет можно получить по итогам игры.
"""

def prefix_sum(input, size):
    prefix_sum = [0] * (size + 1)
    for i in range(1, size + 1):
        prefix_sum[i] = prefix_sum[i - 1] + input[i - 1]
    return prefix_sum

def calc_max(input, num):
    size = len(input)
    if num >= size:
        return sum(input)
    prefix = prefix_sum(input, size)
    print(prefix)
    max_sum = 0
    for i in range(num + 1):
        sum_lr = prefix[i] + (prefix[size] - prefix[size-num + i])
        if sum_lr > max_sum:
            max_sum = sum_lr
    return max_sum


num = int(input('Число ходов:\n'))
input = list(map(int, input('Массив:\n').split()))
print(calc_max(input, num))
