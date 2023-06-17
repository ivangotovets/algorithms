from math import sqrt


def dist(x1, y1, x2, y2):
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)


def inside_triangle(d, x, y):
    points = {
        '1': (0, 0),
        '2': (d, 0),
        '3': (0, d),
    }
    if (x + y <= d) and (x > 0) and (y > 0):
        return 0
    min_point = '1'
    min_dist = dist(*points[min_point], x, y)
    for point in points:
        if min_dist > dist(*points[point], x, y):
            min_point = point
    return min_point


print(inside_triangle(5, 1, 1))
print(inside_triangle(3, -1, -1))
