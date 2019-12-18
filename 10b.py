import sys
from collections import namedtuple
from math import gcd, acos, hypot, pi

lines = [line.rstrip() for line in sys.stdin]

#print('\n'.join(line for line in lines))
#print()
w = len(lines[0])
h = len(lines)

# Part 1
Point = namedtuple("Point", "x y")

# get a direction vector with integer components. All asteroids on the line in
# direction e from some pov a will then be at point a + n*e for some integer n,
# making the destroyed asteroid easy to find in part b. Also don't have to worry
# about any float inaccuracies when comparing and adding to a set
def int_normed(v):
    div = gcd(v.x, v.y)
    return Point(v.x // div, v.y // div)

def sub(a, b):
    return Point(a.x - b.x, a.y - b.y)

# return unique direction vectors that point to at least one asteroid visible from v
def vis_from(v):
    return {int_normed(sub(a, v)) for a in asteroids if a != v}

asteroids = [Point(x, y) for y in range(h) for x in range(w) if lines[y][x] == '#'] 
vis_dirs = {pov: vis_from(pov) for pov in asteroids}

mon = max(vis_dirs.keys(), key=lambda a: len(vis_dirs[a]))
print(f"Best location is at {mon} with {len(vis_dirs[mon])} visible asteroids\n")

# Part 2. Note that at least for my input there were over 200 visible asteroids
# immediately, so I didn't write any code to handle extra full rotations
# possibly needed by other inputs!

# angle theta between vector v and (0, -1) (pointing upwards) from dot product
def get_angle(v):
    theta = acos(-v.y / hypot(*v))
    if v.x < 0:
        theta = 2*pi - theta
    return theta

def add(a, b):
    return Point(a.x + b.x, a.y + b.y)

last_ray_dir = sorted(vis_dirs[mon], key=get_angle)[199]

curr = add(mon, last_ray_dir)
while curr not in asteroids:
    curr = add(curr, last_ray_dir)
    assert 0 <= curr.x < w
    assert 0 <= curr.y < h

print(f"200th asteroid to be destroyed is at {curr}")
print(f"100 * {curr.x} + {curr.y} = {100 * curr.x + curr.y}")
