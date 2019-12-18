import sys

with open("5-input.txt") as f:
    lines = [line.rstrip() for line in f]
prog = list(map(int, lines[0].split(',')))

# opcode        1  2  3  4
inst_lens = [0, 4, 4, 2, 2]

def parse_inst(inst):
    s = str(inst).zfill(5)
    return map(int, (s[0], s[1], s[2], s[3:]))

def run(prog):
    ip = 0

    while ip < len(prog):
        mode3, mode2, mode1, opcode = parse_inst(prog[ip])
        if opcode == 99:
            return

        #print("ip: {}, opcode: {}, modes: {}{}{}, len: {}".format(ip, opcode, mode3, mode2, mode1, inst_lens[opcode]))
        if inst_lens[opcode] == 4:
            val1, val2 = prog[ip+1], prog[ip+2]
            if mode1 == 0:
                val1 = prog[val1]
            if mode2 == 0:
                val2 = prog[val2]
            tgt = prog[ip+3]

            if opcode == 1:
                prog[tgt] = val1 + val2
            elif opcode == 2:
                prog[tgt] = val1 * val2
        elif inst_lens[opcode] == 2:
            param1 = prog[ip+1]
            if opcode == 3:
                prog[param1] = int(input())
            elif opcode == 4:
                val = param1
                if mode1 == 0:
                    val = prog[val]
                print(val)

        ip += inst_lens[opcode]

    print("Didn't see opcode 99!")

run(prog.copy())
