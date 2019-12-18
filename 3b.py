import sys
import operator

input_lines = [line.rstrip() for line in sys.stdin]

DIRS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
def get_points(line):
    points = []
    prev = (0, 0)
    points.append(prev)

    for cmd in line.split(','):
        dir = cmd[0]
        amt = int(cmd[1:])
        add = list(map(operator.mul, DIRS[dir], (amt, amt)))
        point = list(map(operator.add, prev, add))
        point.append(amt)
        point = tuple(point)

        prev = point
        points.append(point)

    return points

def seg_is_hor(p1, p2):
    return p1[1] == p2[1]

def point_on_segment(p, p1, p2):
    if p1[0] == p2[0] and p1[0] == p[0]:
        return min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1])
    elif p1[1] == p2[1] and p1[1] == p[1]:
        return min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0])
    return False

def intersect(a1, a2, b1, b2):
    if seg_is_hor(a1, a2) and not seg_is_hor(b1, b2):
        pot = (b1[0], a1[1])
    elif not seg_is_hor(a1, a2) and seg_is_hor(b1, b2):
        pot = (a1[0], b1[1])
    else:
        # assume parallel lines don't intersect!
        return []

    ret = []
    if pot != (0, 0) and point_on_segment(pot, a1, a2) and point_on_segment(pot, b1, b2):
        ret.append(pot)
    return ret

def dist(p1, p2=(0,0)):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

points1, points2 = map(get_points, input_lines)
intersecting = []

for i in range(len(points1) - 1):
    a1, a2 = points1[i], points1[i+1]
    for j in range(len(points2) - 1):
        b1, b2 = points2[j], points2[j+1]
        intersecting += intersect(a1, a2, b1, b2)

print(intersecting)
print(min(dist(p) for p in intersecting))

def calc_distances(points):
    seen = set()
    currdist = 0
    for i in range(len(points) - 1):
        a1, a2 = points[i], points[i+1]
        for intpoint in intersecting:
            if point_on_segment(intpoint, a1, a2) and intpoint not in seen:
                seen.add(intpoint)
                dists_to_intersecting[intpoint] += currdist + dist(a1, intpoint)
        currdist += a2[2]

dists_to_intersecting = {p: 0 for p in intersecting}
calc_distances(points1)
calc_distances(points2)
print(dists_to_intersecting)
print(min(dists_to_intersecting.values()))
