import sys

lines = [line.rstrip() for line in sys.stdin]

print(sum(int(num) // 3 - 2 for num in lines))
