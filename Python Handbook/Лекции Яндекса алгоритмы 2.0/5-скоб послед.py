

def brackets(text):
    if len(text) % 2:
        return False
    while len(text) > 0:
        text = text.replace('()','')
    if text == '':
        return True
    else:
        return False


text1 = '(())()'
text2 = '(()))()'

print(brackets(text1))
print(brackets(text2))

