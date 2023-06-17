"""
Напишите генератор cycle, который принимает список и работает
аналогично итератору itertools.cycle.
"""


def cycle(ls):
    while True:
        for elem in ls:
            yield elem


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))

print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))

