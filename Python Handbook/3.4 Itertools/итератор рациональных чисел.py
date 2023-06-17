from itertools import count

text = '3.2 6.4 0.8'
inp = [float(x) for x in text.split(' ')]
for x in count(inp[0], inp[2]):
    if x >= inp[1]:
        break
    print(f'{x:.2f}')