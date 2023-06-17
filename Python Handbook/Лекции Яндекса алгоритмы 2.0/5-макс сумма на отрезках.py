from itertools import product


def prefix_acc(seq, n):
    acc = [0]*(n+1)
    for i in range(1, n+1):
        acc[i] = acc[i-1] + seq[i-1]
    return acc

def sum_interval(acc, i, j):
    if i == j:
        return acc[i]
    return acc[j] - acc[i]


n = 5
text = '5 4 -10 11 17'
seq = [int(x) for x in text.split(' ')]
pref = prefix_acc(seq, n)
max_sum = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        acc = sum_interval(pref, i, j)
        if acc > max_sum:
            max_sum = sum_interval(pref, i, j)

print(max_sum)
