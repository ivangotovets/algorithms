"""
вам даётся запись некоторой корректной даты. Требуется выяснить, однозначно
по этой записи определяется дата даже без дополнительной информации о формате.
"""
from datetime import date


def check_date(date_str):
    acc = [int(x) for x in date_str.split(' ')]
    try:
        not(date(acc[2], acc[1], acc[0])
            and date(acc[2], acc[0], acc[1]))
    except Exception:
        return True
    else:
        return False


print(check_date('1 2 2003'))
print(check_date('2 29 2008'))
