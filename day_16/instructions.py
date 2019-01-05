

def addr(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = input_register[A] + input_register[B]
    return res


def addi(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = input_register[A] + B
    return res


def mulr(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = input_register[A] * input_register[B]
    return res


def muli(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = input_register[A] * B
    return res


def banr(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = input_register[A] & input_register[B]
    return res


def bani(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = input_register[A] & B
    return res


def borr(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = input_register[A] | input_register[B]
    return res


def bori(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = input_register[A] | B
    return res


def setr(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = input_register[A]
    return res


def seti(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = A
    return res

def gtir(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = int(A > input_register[B])
    return res


def gtri(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = int(input_register[A] > B)
    return res


def gtrr(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = int(input_register[A] > input_register[B])
    return res


def eqir(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = int(A == input_register[B])
    return res


def eqri(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = int(input_register[A] == B)
    return res


def eqrr(input_register, instruction):
    res = input_register.copy()
    A, B, C = instruction
    res[C] = int(input_register[A] == input_register[B])
    return res
