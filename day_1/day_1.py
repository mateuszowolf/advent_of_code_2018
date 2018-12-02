import os
import itertools

INPUT_FILE = os.path.join('day_1', 'input.txt')

def part_1():

    start_freq = 0

    with open(INPUT_FILE, 'r') as file:
        for line in file.readlines():
            start_freq += int(line)

    print(f"Part 1 - Result frequency: {start_freq}")

def part_2():

    with open(INPUT_FILE, 'r') as file:
        input = [int(line) for line in file.readlines()]

    numbers = itertools.cycle(input)

    frequencies = set([0])
    curr_freq = 0

    for i in numbers:
        curr_freq += i
        if curr_freq in frequencies:
            break
        else:
            frequencies.add(curr_freq)

    print(f"Part 2 freq {curr_freq}")


if __name__ == '__main__':

    choice = int(input('Which part woud you like to run: \n'))
    if choice == 1:
        part_1()
    if choice == 2:
        part_2()
    else:
        print('only 1 or 2 are covered')