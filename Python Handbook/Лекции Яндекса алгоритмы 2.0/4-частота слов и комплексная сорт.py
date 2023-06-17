from operator import itemgetter, attrgetter

text = 'oh you touch my tralala mmm my ding ding dong'
acc = {}
sorted_words = []
for word in text.split(' '):
    if word not in acc:
        acc[word] = 0
    acc[word] += 1


for key, value in acc.items():
    tmp = (value, key)
    sorted_words.append(tmp)
print(sorted_words)
res = sorted(sorted_words, key=lambda x: (x[0] * -1, x[1]))
for elem in res:
    print(elem)