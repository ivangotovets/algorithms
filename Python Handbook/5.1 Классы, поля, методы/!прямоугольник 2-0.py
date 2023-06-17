"""
Расширим функционал класса написанного вами в предыдущей задаче.

Реализуйте методы:

get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
get_size() — возвращает размеры в виде кортежа;
move(dx, dy) — изменяет положение на заданные значения;
resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).

rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())


(3.2, 3.14) (4.32, 7.44)
(4.52, -1.86) (4.32, 7.44)

"""