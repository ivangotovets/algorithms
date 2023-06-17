def read_inline(file_object):
    while True:
        data = file_object.read()
        if not data:
            break
        yield data

with (
  open('input5.txt', 'r', encoding='UTF-8') as file_in
):
    num = int(input('N='))
    lines = file_in.readlines()
    for line in lines[len(lines)-num:]:
        print(line, end='')