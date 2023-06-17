from itertools import combinations

text = 'Аня Боря Вова'

for x, y in combinations(text.split(' '), r=2):
    print(f'{x} - {y}')