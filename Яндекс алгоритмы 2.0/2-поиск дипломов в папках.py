"""
В первой строке входного файла записано целое число N (1 ≤ N ≤ 100) - количество
папок. Во второй строке записаны N целых чисел a1, a2, ..., aN (1 ≤ ai ≤ 100) -
количество дипломов в каждой из папок.
Выведите одно число - минимальное количество секунд, необходимое Ивану в худшем
случае для определения того, в какой папке содержится диплом.
"""



def search(seq):
    acc = [int(x) for x in seq.split(' ')]
    res = sorted(acc, reverse=True)
    return sum(res[1:])

seq='2 1 3 7'
print(search(seq))