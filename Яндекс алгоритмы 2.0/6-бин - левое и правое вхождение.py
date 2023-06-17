# левый бинарный поиск - функция возрастает
def left_binsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


# правый бинарный поиск - функция убывает
def right_binsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2 + 1
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l

def eq(i, param):
    x, seq = param
    return seq[i] == x

def findleft(seq, x):
    pos = left_binsearch(0, len(seq)-1, eq, (x, seq))
    if not eq(pos, (x, seq)):
        return 0
    return pos+1

def findright(seq, x):
    pos = right_binsearch(0, len(seq)-1, eq, (x, seq))
    if not eq(pos, (x, seq)):
        return 0
    return pos+1

text = '0 1 2 2 2 3'
x = 2

seq = [int(x) for x in text.split(' ')]

print(f'{findleft(seq, x)} {findright(seq, x)}')