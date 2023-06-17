def nearest_shop(pos, list_house):
    MIN_LEFT = 0
    MAX_RIGHT = len(list_house) - 1
    left = pos
    right = pos
    while left >= MIN_LEFT or right <= MAX_RIGHT:
        left -= 1
        right += 1
        if left >= MIN_LEFT and list_house[left] == '2':
            return pos - left
        elif right <= MAX_RIGHT and list_house[right] == '2':
            return right - pos
    return None


def farest_house(seq):
    acc = [x for x in seq.split(' ')]
    cache = {}
    for i, house in enumerate(acc):
        if house == '1':
            cache[i] = nearest_shop(i, acc)
    max_way = max(cache.values())
    for i, house in cache.items():
        if house == max_way:
            print(f'{i+1}-й дом, расстояние - {house}')

seq = '2 0 1 1 0 1 0 2 1 2 0 0 1'

farest_house(seq)

