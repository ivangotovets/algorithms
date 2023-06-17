from itertools import product

text = ['пик', 'треф', 'бубен', 'червей']
cards = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
delete = 'червей'

mast = text.remove(delete)

for x, y in sorted(product(mast, cards), key=lambda x: (x[1],x[0])):
    print(f'{y} {x}')