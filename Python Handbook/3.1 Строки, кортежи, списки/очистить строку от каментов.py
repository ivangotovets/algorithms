"""
Вводятся строки программы.
Признаком остановки является пустая строка.
Формат вывода
Каждую строку нужно очистить от комментариев.
А если комментарий — вся строка, то выводить её не надо.

Ввод
# Моя первая супер-пупер программа
print("What is your name?") # Как тебя зовут?
name = input() # Сохраняем имя print(f"Hello, {name}!") # Здороваемся
# Конец моей супер-пупер программы
Вывод
print("What is your name?")
name = input()
print(f"Hello, {name}!")

"""
line = input()
text = []
while line != "":
    text.append(line)
    line = input()

clean_txt = []
i = 0
while i <= len(text):
    pos = text[i].find('#')
    if pos == 0:
        i += 1
    elif text[i].find('#') != -1:
        clean_txt.append(text[i][:pos])


for line in text:
    print(line)