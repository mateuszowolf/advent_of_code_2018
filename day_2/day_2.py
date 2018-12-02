from collections import Counter
from itertools import combinations, compress
import os

FILE_PATH = os.path.join('day_2', 'input.txt')

def part_1():

    count_2 = 0
    count_3 = 0

    with open(FILE_PATH, 'r') as file:
        for line in file.readlines():
            counts = Counter(line)
            if 2 in counts.values():
                count_2 += 1
            if 3 in counts.values():
                count_3 += 1

    print(f"Count 2: {count_2}")
    print(f"Count 3: {count_3}")
    print(f"Count multiply: {count_2 * count_3}")

def part_2():
    with open(FILE_PATH, 'r') as file:
        words = [line.strip() for line in file.readlines()]

    for one, two in combinations(words, 2):
        diff = [e1 == e2 for e1, e2 in zip(one, two)]
        if sum(diff) == len(one) - 1:
            result = "".join(list(compress(one, diff)))

    print(f"Part 2 result; {result}")




if __name__ == '__main__':
    choice = int(input('Which part woud you like to run: \n'))
    if choice == 1:
        part_1()
    elif choice == 2:
        part_2()
    else:
        print('only 1 or 2 are covered')