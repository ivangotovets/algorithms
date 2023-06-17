

def letters(sentence):
    word_set = set(sentence)
    return ''.join(x for x in word_set)


sentence = 'змееед'
print(letters(sentence))