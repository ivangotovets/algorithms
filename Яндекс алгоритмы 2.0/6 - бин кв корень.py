def sqr(x):
    l = 0
    r = x + 1
    while l + 0.001 < r:
        m = (l + r) / 2
        if m**2 > x:
            r = m
        else:
            l = m
    return int(l)

print(sqr(4))