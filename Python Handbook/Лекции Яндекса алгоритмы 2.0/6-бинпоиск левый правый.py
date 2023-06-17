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

