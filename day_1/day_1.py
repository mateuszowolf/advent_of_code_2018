import os

INPUT_FILE = os.path.join('day_1', 'input.txt')

def part_1():

    start_freq = 0

    with open(INPUT_FILE, 'r') as file:
        for line in file.readlines():
            start_freq += int(line)

    print(f"Part 1 - Result frequency: {start_freq}")

def part_2():
    


if __name__ == '__main__':
    part_1()