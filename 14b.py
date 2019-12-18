from math import ceil
import sys
from collections import defaultdict

lines = [line.rstrip() for line in sys.stdin]

# Part 1
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

#print(reactions)
def run(tgt_fuel):
    global surplus
    surplus = defaultdict(int)
    return get_needed_ore(tgt_fuel, "FUEL")

def get_needed_ore(amt, chem):
    needed_ore = 0
    prod_amt, reqs = reactions[chem]
    iters_needed = ceil(amt / prod_amt)
    surplus[chem] += iters_needed * prod_amt - amt

    for req_amt, req in reqs:
        req_amt *= iters_needed
        if req == "ORE":
            needed_ore += req_amt
            continue

        used_surplus = min(surplus[req], req_amt)
        surplus[req] -= used_surplus
        req_amt -= used_surplus
        needed_ore += get_needed_ore(req_amt, req)

    return needed_ore

print(run(1))

# Part 2
tgt_ore = 1e12
upper = 1
needed = run(upper)

while needed < tgt_ore:
    upper *= 2
    needed = run(upper)
lower = upper // 2

def bin_search(lower, upper):
    while lower <= upper:
        mid = (lower + upper) // 2
        needed = run(mid)

        if needed <= tgt_ore:
            lower = mid + 1
        else:
            upper = mid - 1

    return upper

print(bin_search(lower, upper))
