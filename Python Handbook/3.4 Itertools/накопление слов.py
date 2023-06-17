import operator
from itertools import accumulate

text = 'мама мыла раму'
input = text.split(' ')
for i, x in enumerate(input):
    input[i] += ' '

for x in accumulate(input):
    print(f'{x}')
