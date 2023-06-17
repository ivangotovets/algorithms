"""
Напишите программу,
которая по списку дружественных пар для каждого человека определяет список «друзей 2-го уровня».

Выведите список всех людей и их «друзей 2-го уровня» в формате «Человек: Друг1, Друг2, ...».
Список людей и друзей в каждой строке требуется вывести в алфавитном порядке без повторений.

Иванов Петров
Иванов Сергеев
Васильев Петров
Сергеев Яковлев
Петров Кириллов
Петров Яковлев

Васильев: Иванов, Кириллов, Яковлев
Иванов: Васильев, Кириллов, Яковлев
Кириллов: Васильев, Иванов, Яковлев
Петров: Сергеев
Сергеев: Петров
Яковлев: Васильев, Иванов, Кириллов
"""

friends = (
    ('Иванов', 'Петров'),
    ('Иванов', 'Сергеев'),
    ('Васильев', 'Петров'),
    ('Сергеев', 'Яковлев'),
    ('Петров', 'Кириллов'),
    ('Петров', 'Яковлев'),
)

acc = set()
for elem in friends:
    for surname in elem:
        acc.add(surname)

def find_friends(friend, friends):
    acc = set()
    for elem in friends:
        if friend in elem:
            for surname in elem:
                if surname != friend:
                    acc.add(surname)
    return acc

for friend in sorted(acc):
    acc = set()
    print(f'{friend}', end=': ')
    friends1 = find_friends(friend, friends)
    for friend2 in friends1:
        friends3 = find_friends(friend2, friends)
        acc = acc | friends3
    acc.remove(friend)
    print(' '.join(sorted(acc)))





