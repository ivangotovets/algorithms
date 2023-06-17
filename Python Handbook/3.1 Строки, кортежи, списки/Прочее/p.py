all_leng = int(input('Lenth of line:\n'))
no_string = int(input('No of strings\n'))
accum = []
for i in range(no_string):
    accum.append(input())

for line in accum:
    if len(line)-1 < all_leng:
        print(line)
    print(line[:(all_leng-5)] + '...')