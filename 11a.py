from collections import defaultdict

with open("11-input.txt") as f:
    prog = list(map(int, f.read().rstrip().split(',')))

# opcode        1  2  3  4  5  6  7  8  9
inst_lens = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]

def parse_inst(inst):
    s = str(inst).zfill(5)
    return map(int, (s[0], s[1], s[2], s[3:]))

def extend_mem(prog, new_size):
    prog.extend([0] * (new_size - len(prog)))

def run(prog):
    ip = 0
    base = 0

    while ip < len(prog):
        mode3, mode2, mode1, opcode = parse_inst(prog[ip])
        modes = [0, mode1, mode2, mode3]
        if opcode == 99:
            yield (99, None)

        #print("ip: {}, opcode: {}, modes: {}{}{}, len: {}".format(ip, opcode, mode3, mode2, mode1, inst_lens[opcode]))
        vals = [0]
        for i in range(1, inst_lens[opcode]):
            tgt = prog[ip+i]
            vals.append(prog[ip+i])
            if modes[i] == 0 or modes[i] == 2:
                if modes[i] == 2:
                    vals[i] += base
                    tgt += base
                assert vals[i] >= 0
                if vals[i] >= len(prog):
                    extend_mem(prog, vals[i] + 1)
                vals[i] = prog[vals[i]]

        if opcode == 1:
            prog[tgt] = vals[1] + vals[2]
        elif opcode == 2:
            prog[tgt] = vals[1] * vals[2]
        elif opcode == 3:
            prog[tgt] = (yield (3, None))
        elif opcode == 4:
            yield (4, vals[1])
        elif opcode == 5:
            if vals[1]:
                ip = vals[2]
                continue
        elif opcode == 6:
            if not vals[1]:
                ip = vals[2]
                continue
        elif opcode == 7:
            prog[tgt] = vals[1] < vals[2]
        elif opcode == 8:
            prog[tgt] = vals[1] == vals[2]
        elif opcode == 9:
            base += vals[1]
        else:
            raise NotImplementedError(f"Unimplemented opcode: {opcode}")

        ip += inst_lens[opcode]

    raise RuntimeError("Didn't see opcode 99!")

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def rot_left(d):
    return (dot(d, (0, -1)), dot(d, (1, 0)))

def rot_right(d):
    return (dot(d, (0, 1)), dot(d, (-1, 0)))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

# facing up first
direction = (0, 1)
pos = (0, 0)
visited = defaultdict(int)
robot = run(prog.copy())
opcode, retval = next(robot)

while opcode != 99:
    #print(opcode, retval)
    assert opcode == 3
    #print(visited[pos])
    opcode, retval = robot.send(visited[pos])
    visited[pos] = retval
    opcode, retval = next(robot)
    #print(opcode, retval)
    direction = rot_left(direction) if retval == 0 else rot_right(direction)
    #print(pos, direction)
    pos = add(pos, direction)

    opcode, retval = next(robot)

print(len(visited))
