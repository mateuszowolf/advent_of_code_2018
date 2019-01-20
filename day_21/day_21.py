import sys

sys.path.append('..')

from instructions import *
from day_19.day_19 import INSTRUCTIONS, read_input

def part_1():
    instruction_pointer = 0
    register = [0, 0, 0, 0, 0, 0]
    instruction_register, instructions = read_input()
    c = 0
    while c< 50:
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
        print(c, instruction_pointer, register, funct, instruction)
        register[instruction_register] = instruction_pointer
        register = INSTRUCTIONS[funct](register, instruction)
        instruction_pointer = register[instruction_register] + 1
        c+=1

if __name__ == '__main__':
    print(part_1())

