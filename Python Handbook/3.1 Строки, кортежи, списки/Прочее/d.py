"""
Напишите программу, которая избавляется от:
* Двух символов # в начале информационных сообщений;
* Строк, заканчивающихся тремя символами @.

Ввод
First Message
##Second Message
@@@Third Message##
##Fourth Message@@@
Вывод
First Message
Second Message
@@@Third Message##
"""
print('Input log, empty string for exit:')
text = []
log = input()
while log != '':
    text.append(log)
    log = input()

for i in range(len(text)):
    if text[i].startswith('##'):
        text[i] = text[i][2:]
    if text[i].endswith('@@@'):
        del text[i]
for line in text:
    print(line)