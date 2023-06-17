def read_inline(file_object):
    while True:
        data = file_object.read()
        if not data:
            break
        yield data


with (
    open('input4.txt', 'r', encoding='UTF-8') as file_in,
    open('output4.txt', 'w', encoding='UTF-8') as file_out,
):
    for line in read_inline(file_in):
        line = line.strip('\n').replace('	', '').replace('  ', '')
        if line != '\n':
            file_out.write(line)
