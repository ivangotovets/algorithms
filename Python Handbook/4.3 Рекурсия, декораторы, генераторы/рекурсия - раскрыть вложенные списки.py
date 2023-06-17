"""
Раскрыть список списков
"""


array_to_parse_1 = ([-1, [1, [-2], 1], -1])
array_to_parse_2 = ([1, [2, 2, 2], 4])


def parse_list(input_array):
    result_array = []
    for array_item in input_array:
        if isinstance(array_item, list) or isinstance(array_item, tuple):
            result_array += parse_list(array_item)
        else:
            result_array.append(array_item)
    return result_array


print(parse_list(array_to_parse_1))
print(parse_list(array_to_parse_2))