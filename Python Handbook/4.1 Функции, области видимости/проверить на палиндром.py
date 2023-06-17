"""
Напишите функцию is_palindrome, которая принимает натуральное число, строку,
кортеж или список, а возвращает логическое значение: True — если передан
палиндром, а в противном случае — False.

"""

def is_palindrome(line):
    if type(line) == int:
        acc = str(line)[::-1]
    else:
        acc = line[::-1]
    if acc =