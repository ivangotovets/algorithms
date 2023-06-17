def dist(t, params):
    x, v = params
    minpos = maxpos = x[0] + v[0]*t
    for i in range(1, len(x)):
        nowpos = x[i] + v[i] * t
        minpos = min(minpos, nowpos)
        maxpos = max(minpos, nowpos)
    return maxpos - minpos


def checkasc(t, eps, params):
    return dist(t + eps, params) >= dist(t, params)


def fbinsearch(l, r, eps, check, params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, eps, params):
            r = m
        else:
            l = m
    return l

