from collections import defaultdict

with open("13-input.txt") as f:
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
            return (99, None)

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

p = prog.copy()
p[0] = 2
game = run(p)

score = 0
ball = paddle = (-1, -1)
ball_dir = 1
grid = []

def handle_output(x, y, id):
    global ball, paddle, ball_dir, score
    if x == -1 and y == 0:
        score = id
        return

    if y >= len(grid):
        grid.append([])
    if x >= len(grid[y]):
        grid[y].append(-1)

    grid[y][x] = id
    if id == 3:
        paddle = (x, y)
    elif id == 4:
        ball_dir = 1 if x > ball[0] else -1
        ball = (x, y)
    #print(x, y, id)

def handle_input():
    diff = ball[0] - paddle[0]
    ydiff = paddle[1] - ball[1]
    #print(ball_dir, diff)

    # ball going right
    if ball_dir == 1:
        if diff == 0:
            return ball_dir if ydiff > 1 else 0
        # ball to the right of paddle
        elif diff > 0:
            return ball_dir
        elif diff == -1:
            return 0
        else:
            return -1
    elif ball_dir == -1:
        if diff == 0:
            return ball_dir if ydiff > 1 else -ball_dir
        elif diff < 0:
            return ball_dir
        elif diff == 1:
            return 0
        else:
            return 1

charmap = [' ', '#', '.', '-', 'o']

def print_grid():
    print('\n'.join(''.join(charmap[id] for id in line) for line in grid))
    print(f"Score: {score}")
    print()

opcode, val = next(game)
while True:
    # game outputs grid state three values at a time, so if we see one output
    # read the other two right after
    try:
        if opcode == 4:
            x = val
            y, id = next(game)[1], next(game)[1]
            handle_output(x, y, id)
            opcode, val = next(game)
        elif opcode == 3:
            print_grid()
            opcode, val = game.send(handle_input())
    except:
        print(f"Final score: {score}")
        break
