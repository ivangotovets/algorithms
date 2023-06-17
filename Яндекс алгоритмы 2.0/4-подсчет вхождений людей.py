
text = ('McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1')

key_sum = {}
for elem in text:
    name_vote = elem.split(' ')
    if name_vote[0] not in key_sum:
        key_sum[name_vote[0]] = int(name_vote[1])
    else:
        key_sum[name_vote[0]] += int(name_vote[1])

for key, votes in key_sum.items():
    print(f'{key}: {votes}')

