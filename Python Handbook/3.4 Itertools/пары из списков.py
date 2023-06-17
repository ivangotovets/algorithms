list1 = 'Аня, Вова'
list2 = 'Боря, Дима, Гена'

list3 = list(zip(list1.split(', '), list2.split(', ')))
for x, y in list3:
    print(f'{x} - {y}')