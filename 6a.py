import sys
from collections import namedtuple, defaultdict

sys.setrecursionlimit(10000)
lines = [line.rstrip().split(')') for line in sys.stdin]

Obj = namedtuple('Obj', "parent orbiters")
objs = defaultdict(lambda: Obj(None, list()))

for obj, orbiter in lines:
    objs[obj].orbiters.append(orbiter)
    objs[orbiter] = objs[orbiter]._replace(parent = obj)

for name, obj in objs.items():
    if obj.parent == None:
        com = name
        break

def dfs(obj, orbits):
    return orbits + sum(dfs(o, orbits + 1) for o in objs[obj].orbiters)

print(dfs(com, 0))
