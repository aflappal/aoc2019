import sys

input_lines = [line.rstrip() for line in sys.stdin]

def get_points(line):
    points = []
    prev = (0, 0)
    points.append(prev)

    for cmd in line.split(','):
        dir = cmd[0]
        amt = int(cmd[1:])
        if dir == "R":
            point = ((prev[0] + amt), prev[1])
        elif dir == "L":
            point = ((prev[0] - amt), prev[1])
        elif dir == "U":
            point = ((prev[0]), prev[1] + amt)
        elif dir == "D":
            point = ((prev[0]), prev[1] - amt)

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

def dist(p):
    return abs(p[0]) + abs(p[1])

points1, points2 = map(get_points, input_lines)
intersecting = []

for i in range(len(points1) - 1):
    a1, a2 = points1[i], points1[i+1]
    for j in range(len(points2) - 1):
        b1, b2 = points2[j], points2[j+1]
        intersecting += intersect(a1, a2, b1, b2)

print(intersecting)
print(min(dist(p) for p in intersecting))
