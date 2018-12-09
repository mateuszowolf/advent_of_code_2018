import os
from collections import defaultdict, Counter
import re

FILE_PATH = os.path.join('day_4', 'input.txt')

def read_sort_file():
    with open(FILE_PATH) as f:
        lines = [(s[1:17], s[18:].strip()) for s in f]
        lines = sorted(lines, key=lambda x: x[0])

    return lines

def part_1():
    lines = read_sort_file()
    guards = defaultdict(list)
    for time, line in lines:
        if '#' in line:
            guard = re.search('#\d+', line).group()
            start, end = None, None
        elif 'falls asleep' in line:
            start = int(time[-2:])
        elif 'wakes up' in line:
            end = int(time[-2:])
            guards[guard].extend(list(range(start, end)))
            start, end = None, None

    longest = sorted(list(guards.values()), key=len, reverse=True)[0]
    for g, l in guards.items():
        if l == longest:
            sleeping_guard = int(g[1:])

    mins = Counter(longest)
    print(mins.most_common(1)[0][0] * sleeping_guard)

def part_2():
    lines = read_sort_file()
    guards = defaultdict(list)
    for time, line in lines:
        if '#' in line:
            guard = re.search('#\d+', line).group()
            start, end = None, None
        elif 'falls asleep' in line:
            start = int(time[-2:])
        elif 'wakes up' in line:
            end = int(time[-2:])
            guards[guard].extend(list(range(start, end)))
            start, end = None, None

    guards = {g: Counter(l).most_common(1) for g, l in guards.items()}
    most_common = sorted(list(guards.values()), key=lambda x: x[0][1], reverse=True)[0][0]
    for g, l in guards.items():
        if l[0] == most_common:
            sleeping_guard = int(g[1:])
    print(sleeping_guard * most_common[0])

if __name__ == '__main__':
    part_1()
    part_2()
