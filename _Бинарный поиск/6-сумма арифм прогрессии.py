"""
Арифметическая прогрессия
Число m , чтобы получилась сумма k + (k+1) .... + (k+m-1) = n
"""

def leftbinsearch(left, right, checkfunc, params):
    while left < right:
        mid = (left + right) // 2
        if checkfunc(mid, params):
            right = mid
        else:
            left = mid + 1
    return left

def checkcount(days, params):
    n, k = params
    return (2 * k + days - 1) * days // 2 >= n

nodays = leftbinsearch(0, 200, checkcount, (200, 10))
print(nodays)
