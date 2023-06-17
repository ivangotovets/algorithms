

def let_freq(text):
    let_count = {}
    max_count = 0
    for letter in text:
        if letter not in let_count:
            let_count[letter] = 0
        max_count = max(max_count, let_count[letter])
        let_count[letter] += 1
    if let_count.get(' '):
        del let_count[' ']
    sorted_sym = sorted(let_count.keys())
    for row in range(max_count, 0, -1):
        for sym in sorted_sym:
            if let_count[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorted_sym))


text = 'березка елочка зайка волк березка'
let_freq(text)