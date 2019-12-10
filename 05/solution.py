# /usr/bin/env python


def get_opcode(inst):
    opcode = int(str(inst)[-2:])
    a, b, c = 0, 0, 0
    if len(str(inst)) > 2:
        c = int(str(inst)[-3:-2])
        if len(str(inst)) > 3:
            b = int(str(inst)[-4:-3])
            if len(str(inst)) > 4:
                a = int(str(inst)[-5:-4])
    return (opcode, a, b, c)


def get_value(mode, index, inst):
    if(mode == 0):
        return inst[inst[index]]
    return inst[index]


def set_value(mode, index, inst, value):
    if(mode == 0):
        inst[inst[index]] = value
    else:
        inst[index] = value


def solution_1(instructions, input_value):
    index = 0
    while True:
        (opcode, a, b, c) = get_opcode(instructions[index])
        # print("--")
        # print(opcode, index)
        # print(instructions[0:20])

        step = 0

        if opcode == 1:
            instructions[instructions[index+3]] = get_value(
                c, index+1, instructions) + get_value(b, index+2, instructions)
            step = 4
        elif opcode == 2:
            instructions[instructions[index+3]] = get_value(
                c, index+1, instructions) * get_value(b, index+2, instructions)
            step = 4
        elif opcode == 3:
            if c == 0:
                instructions[instructions[index+1]] = input_value
            else:
                instructions[index+1] = input_value
            step = 2
        elif opcode == 4:
            c_ = instructions[index+1]
            if c == 0:
                c_ = instructions[c_]
            step = 2
            print(c_)
        elif opcode == 5:
            # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the
            # instruction pointer to the value from the second parameter. Otherwise, it
            # does nothing.
            if get_value(c, index+1, instructions) != 0:
                index = get_value(b, index+2, instructions)
            else:
                step = 3
        elif opcode == 6:
            # Opcode 6 is jump-if-false: if the first parameter is zero, it
            # sets the instruction pointer to the value from the second
            # parameter. Otherwise, it does nothing.
            if get_value(c, index+1, instructions) == 0:
                index = get_value(b, index+2, instructions)
            else:
                step = 3
        elif opcode == 7:
            # Opcode 7 is less than: if the first parameter is less than the
            # second parameter, it stores 1 in the position given by the third
            # parameter. Otherwise, it stores 0.
            if get_value(c, index+1, instructions) < get_value(b, index+2, instructions):
                set_value(a, index+3, instructions, 1)
            else:
                set_value(a, index+3, instructions, 0)
            step = 4
        elif opcode == 8:
            # Opcode 8 is equals: if the first parameter is equal to the second
            # parameter, it stores 1 in the position given by the third
            # parameter. Otherwise, it stores 0.
            if get_value(c, index+1, instructions) == get_value(b, index+2, instructions):
                set_value(a, index+3, instructions, 1)
            else:
                set_value(a, index+3, instructions, 0)
            step = 4
        elif opcode == 99:
            return
        else:
            print("Error: ", opcode)
            return
        index += step


if __name__ == "__main__":
    inst = [int(x)
            for x in open('input.txt', 'r').readline().rstrip().split(',')]
    solution_1(inst, 1)
    inst = [int(x)
            for x in open('input.txt', 'r').readline().rstrip().split(',')]
    solution_1(inst, 5)
