from math import ceil
import sys
from collections import defaultdict

lines = [line.rstrip() for line in sys.stdin]

surplus = defaultdict(int)
reactions = dict()

def split_tuple(string):
    spl = string.split(' ')
    return (int(spl[0]), spl[1])

def split_reqs(string):
    return tuple(map(split_tuple, string.split(", ")))

for line in lines:
    req_str, prod_str = line.split(" => ")
    reqs = split_reqs(req_str)
    prod = split_tuple(prod_str)
    reactions[prod[1]] = (prod[0], reqs)

def get_needed_ore(amt, chem):
    needed_ore = 0
    prod_amt, reqs = reactions[chem]
    iters_needed = ceil(amt / prod_amt)
    surplus[chem] += iters_needed * prod_amt - amt

    for i in range(iters_needed):
        for req_amt, req in reqs:
            if req == "ORE":
                needed_ore += req_amt
                continue

            used_surplus = min(surplus[req], req_amt)
            surplus[req] -= used_surplus
            req_amt -= used_surplus
            needed_ore += get_needed_ore(req_amt, req)

    return needed_ore

print(get_needed_ore(1, "FUEL"))
