from itertools import permutations

with open("7-input.txt") as f:
#with open("test7-input.txt") as f:
    prog = list(map(int, f.read().rstrip().split(',')))

# opcode        1  2  3  4  5  6  7  8
inst_lens = [0, 4, 4, 2, 2, 3, 3, 4, 4]


class IO:
    def __init__(this, inp=None, outp=None):
        this.inputs = inp
        this.outputs = outp
    def input(this):
        if this.inputs is None:
            return int(input())
        else:
            return this.inputs.pop(0)

    def print(this, val):
        if this.outputs is None:
            print(val)
        else:
            this.outputs.append(val)


def parse_inst(inst):
    s = str(inst).zfill(5)
    return map(int, (s[0], s[1], s[2], s[3:]))

def run(prog, io):
    ip = 0

    while ip < len(prog):
        mode3, mode2, mode1, opcode = parse_inst(prog[ip])
        modes = [0, mode1, mode2, mode3]
        if opcode == 99:
            return

        #print("ip: {}, opcode: {}, modes: {}{}{}, len: {}".format(ip, opcode, mode3, mode2, mode1, inst_lens[opcode]))
        vals = [0]
        for i in range(1, inst_lens[opcode]):
            tgt = prog[ip+i]
            vals.append(prog[ip+i])
            if modes[i] == 0:
                vals[i] = prog[vals[i]]

        if opcode == 1:
            prog[tgt] = vals[1] + vals[2]
        elif opcode == 2:
            prog[tgt] = vals[1] * vals[2]
        elif opcode == 3:
            prog[tgt] = io.input()
        elif opcode == 4:
            io.print(vals[1])
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
        else:
            raise NotImplementedError(f"Unimplemented opcode: {opcode}")

        ip += inst_lens[opcode]

    raise RuntimeError("Didn't see opcode 99!")

io = IO([0])
io.outputs = io.inputs
highest = 0
for perm in permutations([0, 1, 2, 3, 4]):
    for phase in perm:
        io.inputs.insert(0, phase)
        run(prog.copy(), io)
    highest = max(highest, io.outputs[0])
    io.inputs[0] = 0
print(highest)
