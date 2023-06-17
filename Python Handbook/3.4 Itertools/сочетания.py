from itertools import combinations, combinations_with_replacement

text = 'кофе чай сиги презики'

for x in combinations(text.split(' '), r=2):
    print(', '.join(x))
