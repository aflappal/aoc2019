import operator
import re
import sys
from collections import namedtuple
from functools import reduce

lines = [re.sub("[<>xyz= \n]", '', line) for line in sys.stdin]

Vec = namedtuple("Vec", "x y z")

def add(a, b):
    return Vec(a.x + b.x, a.y + b.y, a.z + b.z)

def get_dir(c1, c2):
    diff = c2 - c1
    if diff < 0:
        return -1
    elif diff > 0:
        return 1
    else:
        return 0

def get_dir_vec(a, b):
    return Vec(*map(get_dir, a, b))

def get_new_vel(moon, curr_vel):
    return reduce(add, (get_dir_vec(moon, other) for other in pos), curr_vel)

def get_tot_energy(pos, vel):
    return get_energy(pos) * get_energy(vel)

def get_energy(vec):
    return sum(map(abs, vec))

pos = [Vec(*map(int, line.split(','))) for line in lines]
vel = [Vec(0, 0, 0)] * 4

for step in range(1000):
    vel = list(map(get_new_vel, pos, vel))
    pos = list(map(add, pos, vel))

energy = sum(map(get_tot_energy, pos, vel))
print(f"Energy: {energy}")
