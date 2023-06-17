from itertools import cycle

text = 'Гречневая Пшённая Овсяная'
s = ''
count = 1
for x in cycle(text.split(' ')):
    if count > 10:
        break
    s += ' ' + x
    count += 1
print(s)