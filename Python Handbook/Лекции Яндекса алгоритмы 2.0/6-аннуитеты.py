"""
Дана x - %ставка по кредиту, срок кредита n мес, сумма - m руб
"""


# бинпоиск для вещественных чисел
def fbinsearch(l ,r ,eps , check, param):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, param):
            r = m
        else:
            l = m
    return l


def month_perc(mperc, yperc):
    msum = 1 + mperc / 100
    ysym = 1 + yperc / 100
    return msum ** 12 >= ysym


def checkcredit(mpay, params):
    periods, creditsum, mperc = params
    for i in range(periods):
        percpay = creditsum * (mperc / 100)
        creditsum -= mpay - percpay
    return creditsum <= 0

yperc = 12
eps = 0.001
creditsum = 10000000
periods = 300
mperc = fbinsearch(0, yperc, eps, month_perc, yperc)
mpay = fbinsearch(0, creditsum, eps, checkcredit, (periods, creditsum, mperc))
print(f'{mpay:.3f}')
