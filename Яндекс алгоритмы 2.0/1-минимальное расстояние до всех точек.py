"""
План деревни можно представить в виде прямой, в некоторых целочисленных точках
которой находятся дома учеников. Школу также разрешается строить только в
целочисленной точке этой прямой (в том числе разрешается строить школу в точке,
где расположен один из домов – ведь школа будет расположена с другой стороны улицы).
Напишите программу, которая по известным координатам домов учеников поможет
определить координаты места строительства школы.

1 2 3 4
3
"""
from math import sqrt


def calc_dist(x, *args):
    acc = sum((x - y) ** 2 for y in args)
    return int(sqrt(acc))


def nearest_point(*args):
    min_point = args[0]
    min_dist = calc_dist(min_point, *args)
    for x in range(min(*args), max(*args) + 1):
        dist = calc_dist(x, *args)
        if dist < min_dist:
            min_point = x
            min_dist = dist
    return min_point


print(nearest_point(1, 2, 50))
