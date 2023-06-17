import json


def read_inline(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


with (
    open('input7.json', 'r', encoding='UTF-8') as file_in,
    open('output7.json', 'w', encoding='UTF-8') as file_out,
):
    for line in read_inline(file_in):
        data = json.loads(line)
        data['count'] = 0
        json.dump(data, file_out, ensure_ascii=False)
        file_out.write('\n')