import sys
from itertools import cycle

lines = [line.rstrip() for line in sys.stdin]
curr = list(map(int, lines[0]))
pat = (0, 1, 0, -1)
print(len(curr))

for _ in range(100):
    nums = []
    for i in range(1, len(curr) + 1):
        dig = []
        zeros = 0
        it = cycle(pat)
        curlen = 0
        mul = next(it)
        times = i-1

        while curlen < len(curr):
            if mul == 0:
                zeros += times
            elif mul == 1:
                dig.extend(curr[curlen : curlen+times])
            else:
                dig.extend(list(map(lambda n: -n, curr[curlen : curlen+times])))
            curlen = len(dig) + zeros
            mul = next(it)
            times = min(i, len(curr)-curlen)

        #print(dig)
        nums.append(abs(sum(dig)) % 10)

    #print(nums)
    curr = nums

print(''.join(map(str, curr[:8])))
