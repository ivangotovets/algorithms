def fbinseartch(l, r, eps, checkfunc, params):
    while l + eps < r:
        m = (l + r) / 2
        if checkfunc(m, params):
            r = m
        else:
            l = m
    return l


def cube_eq(x, params):
    a, b, c, d = params
    eq = a * x**3 + b * x**2 + c * x + d
    if a > 0:
        return eq >= 0
    else:
        return eq <= 0


data = (1, -3, 3, -1)
eps = 0.001


res = fbinseartch(-1000, 1000, eps, cube_eq, data)
print(f'{res:.5f}')
