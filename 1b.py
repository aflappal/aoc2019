import sys

lines = [line.rstrip() for line in sys.stdin]

fuel_sum = 0
for line in lines:
    curr = int(line)
    while curr > 0:
        curr = curr // 3 - 2
        if curr > 0:
            fuel_sum += curr

print(fuel_sum)
