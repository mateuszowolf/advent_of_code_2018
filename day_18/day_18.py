import numpy as np
import datetime

def read_input():
    inp = []
    fill_line = '*'
    with open('input.txt') as f:
        first_line = f.readline().strip()
        line_len = len(first_line)
        fill_line *= line_len+2
        inp.append(list(fill_line))
        inp.append(list('*' + first_line + '*'))
        for line in f:
            line = '*' + line.strip() + '*'
            inp.append(list(line))
        inp.append(list(fill_line))

    return np.array(inp)


def solve(mins):
    area = read_input()

    minutes = mins
    lookup = {}

    for i in range(1, minutes+1):
        area = calculate_new_area(area, lookup)
        # print(f'End of minute {i}')
        if i> 1500 and i % 28 == minutes % 28:
            wood = (area == '|').sum()
            lumberyards = (area == '#').sum()
            print(f"{i} {wood*lumberyards}")
            return wood*lumberyards

    wood = (area == '|').sum()
    lumberyards = (area == '#').sum()
    return wood * lumberyards


def get_neighbours(x, y, area):
    return tuple(sorted(area[y-1:y+2, x-1].tolist() + [area[y-1, x]] + [area[y+1, x]] + area[y-1:y+2, x+1].tolist()))


def calculate_new_area(area, lookup):
    area_copy = area.copy()

    for y in range(1, len(area)-1):
        for x in range(1, len(area[y])-1):
            state = area[y, x]
            neigbours = get_neighbours(x, y, area)
            try:
                new_state = lookup[(state, neigbours)]
            except KeyError:
                new_state = evolution_logic(state, neigbours)
                lookup[(state, neigbours)] = new_state
            area_copy[y, x] = new_state

    return area_copy


def evolution_logic(current_state, neighbours):
    if current_state == '.':
        if neighbours.count('|') > 2:
            return '|'
    if current_state == '|':
        if neighbours.count('#') > 2:
            return '#'
    if current_state == '#':
        if not(neighbours.count('#') > 0 and neighbours.count('|') > 0):
            return '.'
    return current_state


if __name__ == '__main__':
    stt = datetime.datetime.now()
    print('Part 1 - 10 minutes')
    print(solve(10))
    print(f"solved in {(datetime.datetime.now() - stt).total_seconds()}")
    stt = datetime.datetime.now()
    print('Part 2 - 1000000000 minutes')
    print(solve(1000000000))
    print(f"solved in {(datetime.datetime.now() - stt).total_seconds()}")
