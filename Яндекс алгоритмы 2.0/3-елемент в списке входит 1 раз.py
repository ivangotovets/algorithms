

def single_elem(text):
    acc = [int(x) for x in text if x != ' ']
    freq = {}
    for elem in acc:
        if elem not in freq:
            freq[elem] = 0
        freq[elem] += 1

    return ' '.join(str(x) for x in freq.keys() if freq[x] == 1)



text = '1 2 2 3 3 3 5 7 2 3 9 2'

print(single_elem(text))