from itertools import permutations

text = 'аня вова боря'

for x in permutations(sorted(text.split(' '))):
    print(' '.join(x))
