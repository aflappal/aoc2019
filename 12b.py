import operator
import re
import sys
from itertools import repeat
from math import gcd

lines = [re.sub("[<>xyz= \n]", '', line) for line in sys.stdin]

def get_dir(c1, c2):
    diff = c2 - c1
    if diff < 0:
        return -1
    elif diff > 0:
        return 1
    else:
        return 0

def get_new_vel(coord, curr_vel, pos):
    return curr_vel + sum(get_dir(coord, other) for other in pos)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(a, b, c):
    return lcm(a, lcm(b, c))

def run(axis):
    pos = [list(map(int, line.split(',')))[axis] for line in lines]
    vel = [0] * 4

    init_state = (*pos, *vel)
    curr_state = None
    steps = 0
    while curr_state != init_state:
        steps += 1
        vel = list(map(get_new_vel, pos, vel, repeat(pos)))
        pos = list(map(operator.add, pos, vel))
        curr_state = (*pos, *vel)

    return steps

periods = [run(axis) for axis in range(3)]
print(periods)
print(lcmm(*periods))
