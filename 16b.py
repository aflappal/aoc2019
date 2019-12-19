import sys
from itertools import accumulate

inp = input()
start = int(inp[:7])
curr = tuple(map(int, inp)) * 10000
curr = reversed(curr[start:])

for _ in range(100):
    curr = accumulate(curr)

ans = map(lambda n: str(n % 10), reversed(tuple(curr)[-8:]))
print(*ans, sep='')
