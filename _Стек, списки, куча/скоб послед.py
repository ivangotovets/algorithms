"""
Определить, является ли скобочная последовательность правильной.
"""
from collections import deque

def brackets(text):
    if len(text) % 2 == 1:
        return False
    acc = deque()
    for letter in text:
        if letter == '(':
            acc.append(letter)
        else:
            acc.pop()
    if acc:
        return False
    return True


text1 = '(())()'
text2 = '(()))()'

print(brackets(text1))
print(brackets(text2))

