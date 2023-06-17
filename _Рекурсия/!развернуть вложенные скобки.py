array_to_parse_1 = ((-1, (1, (-2), 1), -1))


def parse_seq(input):
    result = []
    for elem in input:
        if isinstance(elem, list) or isinstance(elem, tuple):
            result += parse_seq(elem)
        else:
            result.append(elem)
    return result

print(parse_seq(array_to_parse_1))