import sys

lines = [line.rstrip() for line in sys.stdin]
prog = list(map(int, lines[0].split(',')))

def run(noun, verb, prog):
    prog[1] = noun
    prog[2] = verb

    for ip in range(0, len(prog), 4):
        opcode = prog[ip]
        if opcode == 99:
            print("Run finished")
            print(prog)
            return prog[0]

        param1, param2 = prog[ip+1], prog[ip+2]
        tgt = prog[ip+3]
        if opcode == 1:
            prog[tgt] = prog[param1] + prog[param2]
        elif opcode == 2:
            prog[tgt] = prog[param1] * prog[param2]

    print("Didn't see opcode 99!")

print(run(12, 2, prog))
