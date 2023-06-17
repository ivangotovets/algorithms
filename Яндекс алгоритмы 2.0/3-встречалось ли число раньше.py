

text = '1 2 3 2 3 4'


def is_before(text):
    acc = set()
    numbers = [int(x) for x in text.split(' ')]
    print(numbers)
    for elem in numbers:
        if elem in acc:
            print('yes', end=' ')
        else:
            print('no', end= ' ')
        acc.add(elem)

is_before(text)