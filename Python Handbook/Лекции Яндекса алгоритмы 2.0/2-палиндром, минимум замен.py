def min_letters(word):
    acc = list(word)
    max_iter = len(acc) // 2
    if max_iter == 0:
        return 0
    reverse = acc[:max_iter:-1]
    count = 0
    for i in range(max_iter):
        if acc[i] != reverse[i]:
            count += 1
    return count


word1 = 'cognitive'
word2 = 'a'

print(min_letters(word1))
print(min_letters(word2))