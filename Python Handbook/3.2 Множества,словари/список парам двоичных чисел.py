def binary(num):
    bin_dig = [num % 2]
    while num // 2 > 0:
        num = num // 2
        bin_dig.append(num % 2)
    return int(''.join(str(x) for x in bin_dig[::-1]))


def calc_stat(num):
    stat = {
        'digits': 0,
        'units': 0,
        'zeros': 0,
    }
    while num > 0:
        if num % 10 == 1:
            stat['units'] += 1
        if num % 10 == 0:
            stat['zeros'] += 1
        stat['digits'] += 1
        num = num // 10
    return stat


def num_param(text):
    input = [int(x) for x in text.split(' ')]
    acc = []
    for num in input:
        bin_num = binary(num)
        stat = calc_stat(bin_num)
        acc.append(stat)
    for elem in acc:
        print(elem)


text = '5 8 12'
num_param(text)

