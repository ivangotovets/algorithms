

def equal_letters(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    return ''.join(x for x in set2.intersection(set1))


word1 = 'змееед'
word2 = 'велосипед'


print(equal_letters(word1, word2))