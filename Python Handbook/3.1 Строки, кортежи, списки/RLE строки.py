"""
RLE
Не решена
RLE означает “run-length encoding”. Это способ сокращённой записи
последовательности чего угодно (в случае этой задачи — цифр).
При нём для подряд идущей группы одинаковых цифр (run) записываются сама эта
цифра и длина этой группы (run length). Таким образом, 99999 превратится в 9 5
(«девять пять раз») и так далее. RLE широко используется в самых разных областях.
Напишите программу, которая кодирует строку цифр в RLE.

Формат ввода
Строка цифр длиной не меньше 1.

010000100001111111110111110000000000000011111111

0 1
1 1
0 4
1 1
0 4
1 9
0 1
1 5
0 14
1 8
"""

to_encode = '010000100001111111110111110'
accum = [int(x) for x in list(to_encode)]
print(accum)


def find_next(seq, start):
    cur = start
    cur += 1
    while (cur < len(seq)) and (seq[cur] == seq[start]):
        cur += 1
    return cur

def encode(seq):
    cur = 0
    while cur <= len(seq) - 1:
        next = find_next(seq, cur)
        no_digit = next - cur
        print(f'{seq[cur]} {no_digit}')
        cur = next


encode(to_encode)
