def same_surname(input):
    text = input.split(' ')
    acc = {}
    for word in text:
        if word not in acc:
            acc[word] = 0
        acc[word] += 1
    for key in sorted(acc.keys()):
        if acc[key] > 1:
            print(f'{key}: {acc[key]}')


text = 'Иванов Петров Сидоров Петров Иванов Петров'
same_surname(text)
