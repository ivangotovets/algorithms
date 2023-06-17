"""
-->
Аня 160 162
Боря 165 172
Вова 165 165
<--
3
"""
from sys import stdin

acc = {}
res = 0

lines = stdin.readlines()
for line in lines:
    std_data = line.split(' ')
    acc[std_data[0]] = (std_data[1], std_data[2])

for diff in acc.values():
    res += int(diff[1]) - int(diff[0])

print(round(res/len(acc)))
