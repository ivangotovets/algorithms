def same_elem(acc1, acc2):
    ls1 = acc1.split(' ')
    ls2 = acc2.split(' ')
    return len(set(ls1).intersection(set(ls2)))


acc1 = '1 3 2'
acc2 = '5 2 3 6'

print(same_elem(acc1, acc2))