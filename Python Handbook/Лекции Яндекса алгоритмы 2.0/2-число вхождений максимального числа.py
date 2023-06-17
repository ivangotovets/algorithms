
def max_num(seq):
    acc = [int(x) for x in seq.split(' ')]
    max_value = acc[0]
    count = 1
    for x in acc[1:]:
        if max_value < x:
            max_value = x
            count = 1
        elif x == max_value:
            count += 1
    return f'{max_value}: {count}'

seq = '1 1 1 1'
print(max_num(seq))
