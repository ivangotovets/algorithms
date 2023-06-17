from itertools import product

for x, y in product(range(1, 4), range(1, 4)):
    print(f'{x*y} ', end='')
    if y == 3:
        print()
