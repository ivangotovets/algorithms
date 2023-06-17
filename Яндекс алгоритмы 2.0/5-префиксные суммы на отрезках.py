N = 100
acc = [0] * N
pref = [0]*(N+1)

for i in range(N):
    acc[i] = i

pref[0] = 0
for i in range(N+1):
    pref[i] = acc[i-1] + pref[i-1]

key = input('Интервал\n')
while key != 'q':
    l_r = [int(x) for x in key.split(' ')]
    print(f'сумма на отрезке {l_r[0]} - {l_r[1]} = '
          f'{pref[l_r[1]] - pref[l_r[0]]}')
    key = input('Интервал\n')
