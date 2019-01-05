import re
from collections import Counter
from pprint import pprint as print
from copy import deepcopy
from instructions import *

PATTERN = re.compile('\d+')
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

def read_part_1():
    with open('input_p1.txt') as f:
        while f:
            before = list(map(int, re.findall(PATTERN, f.readline())))
            operation = list(map(int, re.findall(PATTERN, f.readline())))
            after = list(map(int, re.findall(PATTERN, f.readline())))
            if not before:
                raise StopIteration
            yield before, operation, after
            _ = f.readline()

def read_part_2():
    with open('input_p2.txt') as f:
        for line in f:
            yield list(map(int, re.findall(PATTERN, line)))

def part_1():
    stats = {k: Counter() for k in INSTRUCTIONS.keys()}
    counter = 0

    for before, operation, after in read_part_1():
        matches = 0
        for label, fun in INSTRUCTIONS.items():
            b = before.copy()
            opcode = operation[0]
            result = fun(b, operation[1:])
            if result == after:
                matches += 1
                stats[label][opcode] += 1
        if matches >= 3:
            counter += 1

    return counter, stats

def translate_opcodes(stats):
    stats_copy = deepcopy(stats)
    opcodes = {}
    while stats_copy:
        f = [k for k, v in stats_copy.items() if len(v) == 1][0]
        opcode = list(stats_copy[f].keys())[0]
        # opcodes[opcode] = f
        opcodes[opcode] = globals()[f]
        del stats_copy[f]

        for rem, counter in stats_copy.items():
            if opcode in counter:
                del counter[opcode]
    return opcodes

def part_2(opcodes):
    register = [0, 0, 0, 0]

    for instruction in read_part_2():
        register = opcodes[instruction[0]](register, instruction[1:])

    return register



if __name__ == '__main__':
    p1_result, stats = part_1()
    print(f"Part 1 results: {p1_result}")
    opcodes = translate_opcodes(stats)
    # print(opcodes)
    p2_result = part_2(opcodes)
    print(p2_result)
    print(f"Part 2 result: {p2_result[0]}")