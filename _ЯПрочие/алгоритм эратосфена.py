"""
Напишите функцию is_prime, которая принимает натуральное число, а возвращает
булево значение: True — если переданное число простое, а иначе — False.
обычный и решето эратосфена
"""
n = int(input("n="))
a = [x for x in range(1, n+1)]
print(a)
lst = [1]

i = 1

while i <= n:

    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1

print(lst)




