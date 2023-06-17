max = 3
ls1 = [1, 2]
ls2 = [2, 1]
ls3 = [1, 0]


def findpos(max, ls1, ls2, ls3):
    for i, x in enumerate(ls1):
        if x < max:
            for j, y in enumerate(ls2):
                if x + y < max:
                    for k, z in enumerate(ls3):
                        if x + y + z == max:
                            return f'{i}, {j}, {k}'
    return -1

print(findpos(max, ls1, ls2, ls3))
