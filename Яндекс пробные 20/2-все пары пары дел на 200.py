

def num_pairs(input):
    calc = 0
    max_cur = len(input)
    for i in range(0, max_cur-1):
        for j in range(i+1, max_cur):
            if abs(input[i] - input[j]) % 200 == 0:
                calc += 1
    return calc

input = list(map(int, input('Массив:\n').split()))

print(num_pairs(input))