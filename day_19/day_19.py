import time
from instructions import *

INSTRUCTIONS = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}


def read_input():
    with open('input.txt') as f:
        ip = int(f.readline().strip()[-1])
        instructions = {}
        for i, line in enumerate(f):
            if not line.strip():
                break
            t = line.strip().split()
            # t[1:] = list(map(int, t[1:]))
            instructions[i] = (t[0], list(map(int, t[1:])))
    return ip, instructions


def part_1():
    instruction_pointer = 0
    register = [0, 0, 0, 0, 0, 0]
    instruction_register, instructions = read_input()
    while True:
        """
        get the value of instruction pointer
        try to retrieve instruction with key instruction pointer
        set register[instruction_register] to instruction pointer
        execute instruction on register
        get value of instruction pointer from instruction register and increment it by 1, set new instruction pointer
        except: catch key error and return register
        """
        try:
            funct, instruction = instructions[instruction_pointer]
        except KeyError:
            return register

        register[instruction_register] = instruction_pointer
        register = INSTRUCTIONS[funct](register, instruction)
        instruction_pointer = register[instruction_register] + 1


def part_2():
    instruction_pointer = 0
    register = [1, 0, 0, 0, 0, 0]
    instruction_register, instructions = read_input()
    c = 0
    while True:
        """
        get the value of instruction pointer
        try to retrieve instruction with key instruction pointer
        set register[instruction_register] to instruction pointer
        execute instruction on register
        get value of instruction pointer from instruction register and increment it by 1, set new instruction pointer
        except: catch key error and return register
        """
        try:
            funct, instruction = instructions[instruction_pointer]
        except KeyError:
            print(instruction_pointer)
            return register


        register[instruction_register] = instruction_pointer
        print(funct, instruction, register, instruction_pointer, sep='  ')
        register = INSTRUCTIONS[funct](register, instruction)
        if instruction_pointer == 3:
            c +=1
            if c == 3:
                register[1] = 10551320
                register[2] = 10551330
                register[5] = 10551329
        instruction_pointer = register[instruction_register] + 1


if __name__ == '__main__':
    print(part_2())