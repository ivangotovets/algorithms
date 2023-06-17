ru_eng = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TC',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA',
}

with (
    open("input.txt", "r", encoding="UTF-8") as file_in,
    open("output.txt", "a", encoding="UTF-8") as file_out
):
    for line in file_in:
        acc = ''
        for sym_eng in line:
            trans_up = ru_eng[sym_eng.upper()] if sym_eng.isalpha() else sym_eng
            acc += trans_up.lower() if sym_eng.islower() else trans_up
        file_out.write(acc)
