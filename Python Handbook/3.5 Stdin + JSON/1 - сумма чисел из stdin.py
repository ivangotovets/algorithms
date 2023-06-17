"""
-->
1 2
3 4 5
6
7 8 9 10

<--
55
"""

from sys import stdin

lines = [line.rstrip('\n') for line in stdin]
inp_str = [int(x) for x in (' '.join(lines)).split(' ')]
print(sum(inp_str))
