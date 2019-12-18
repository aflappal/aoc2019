import sys
from collections import namedtuple, defaultdict
from math import gcd

lines = [line.rstrip() for line in sys.stdin]

print('\n'.join(line for line in lines))
w = len(lines[0])
h = len(lines)

Point = namedtuple("Point", "x y")
def int_norm(v):
    div = gcd(v.x, v.y)
    return Point(v.x // div, v.y // div)

def diff(a, b):
    return Point(a.x - b.x, a.y - b.y)

asteroids = [Point(x, y) for y in range(h) for x in range(w) if lines[y][x] == '#']

vis = defaultdict(set)
for pov in asteroids:
    for a in asteroids:
        if pov == a:
            continue
        d = diff(a, pov)
        vis[pov].add(int_norm(d))

print(max(map(len, vis.values())))
