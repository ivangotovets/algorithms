from math import sqrt

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, move_x=0, move_y=0):
        self.x += move_x
        self.y += move_y

    def length(self, new_point):
        dist = round(sqrt((new_point.x-self.x)**2
                          +(new_point.y-self.y)**2),2)
        return dist


first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
