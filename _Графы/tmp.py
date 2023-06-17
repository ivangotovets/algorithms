
n = b'00000000000000000000000000001011'
n = n.decode('utf-8')
acc = [int(x) for x in str(n)]
count = 0
for x in acc:
    if x == 1:
        count += 1
print(count)