from operator import mul, sub, add

oper = {
        '*': mul,
        '+': add,
        '-': sub,
}


def calc(expr):
    line = expr.split(' ')
    acc = []
    for i in range(len(line)):
        if line[i] in oper:
            res = oper[line[i]](acc.pop(-1), acc.pop(-1))
            acc.append(res)
        else:
            acc.append(int(line[i]))
    return acc[0]


expr = '10 15 - 7 *'

print(calc(expr))
