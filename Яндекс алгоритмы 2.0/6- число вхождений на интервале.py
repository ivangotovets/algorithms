"""
Быстрый поиск в массиве
"""

def lbinsearch(l, r, check, params):
    while l < r:
        m = (l + r) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1
    return l

def gte(i, param):
    x, seq = param
    return seq[i] >= x

def gt(i, param):
    x, seq = param
    return seq[i] > x

def findfirst(seq, x, checkfunc):
    pos = lbinsearch(0, len(seq)-1, checkfunc, (x, seq))
    if not checkfunc(pos, (x, seq)):
        return len(seq)
    else:
        return pos

text = '10 1 10 3 5 7'
acc = [int(x) for x in text.split(' ')]
acc = sorted(acc)
l, r = 1, 10
leftpos = findfirst(acc, l, gte)
rightpos = findfirst(acc, r, gt)
print(f'{rightpos - leftpos}')



