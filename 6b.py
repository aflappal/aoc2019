import sys
from collections import namedtuple, defaultdict

sys.setrecursionlimit(10000)
lines = [line.rstrip().split(')') for line in sys.stdin]

Obj = namedtuple("Obj", "parent orbiters")
objs = defaultdict(lambda: Obj(None, []))

for obj, orbiter in lines:
    objs[obj].orbiters.append(orbiter)
    objs[orbiter] = objs[orbiter]._replace(parent = obj)

# Part 1
# the root is named "COM" in the puzzle, but in case it wasn't:
for name, obj in objs.items():
    if obj.parent == None:
        com = name
        break

def dfs(obj, orbits):
    return orbits + sum(dfs(o, orbits + 1) for o in objs[obj].orbiters)

print(dfs(com, 0))


# Part 2
def get_parents(obj):
    pars = []
    par = objs[obj].parent
    while par != None:
        pars.append(par)
        par = objs[par].parent

    return pars

you_pars, san_pars = map(get_parents, ["YOU", "SAN"])
for par in you_pars:
    if par in san_pars:
        nearest_common = par
        break

print(you_pars.index(nearest_common) + san_pars.index(nearest_common))
