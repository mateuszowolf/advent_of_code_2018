import re
import numpy as np
import networkx as nx
from pprint import pprint as print

def read_input():
    with open('input.txt', 'r') as f:
        depth = int(re.findall('\d+',f.readline())[0])
        target = tuple(map(int, re.findall('\d+', f.readline())))

    return depth, target


def part_1(border = False, multiplier = 2):
    depth, target = read_input()
    """
    create 2 rectangular arrays gi and el
    shape of both = target.y, target.x
    calculate gi for first row and first column
    calculate el for first row and first column
    then for x in range(1, gi.shape[1])
        for y in range(1, gi.shape[0])
            calculate gi using el of squares above and to the left
            calculate el using modulo
            
    risk_level = el % 3
    :return sum
    """
    height = int((target[1] + 1) + (multiplier * target[1] * border))
    width = int((target[0] + 1) + (multiplier * target[0] * border))

    gi = np.zeros((height, width), dtype=int)
    el = np.zeros_like(gi)

    for x in range(1, gi.shape[1]):
        gi[0, x] = x * 16807
    for y in range(1, gi.shape[0]):
        gi[y, 0] = y * 48271

    el = (gi + depth) % 20183

    for x in range(1, gi.shape[1]):
        for y in range(1, gi.shape[0]):
            if (x, y) == target:
                continue
            geo_ind = el[y, x-1] * el[y-1, x]
            gi[y, x] = geo_ind
            el[y, x] = (geo_ind + depth) % 20183

    return el % 3


def print_cavern(el):
    rl = el % 3
    legend = {0: '.', 1: '=', 2: '|'}

    for y in range(rl.shape[0]):
        for x in range(rl.shape[1]):
            print(legend[rl[y, x]], end="")
        print()


def part_2():
    regions = part_1(border=True, multiplier=2)
    regions = regions.astype(str)
    regions[regions == '0'] = '.'
    regions[regions == '1'] = '='
    regions[regions == '2'] = '|'

    _, (tx, ty) = read_input()

    allowed_tools = {
        '.': ('CG', 'T'),
        '=': ('CG', 'N'),
        '|': ('T', 'N')
    }
    # print(regions.shape[0] * regions.shape[1])

    G = nx.Graph()

    """
    create graph
    for each region in regions,
        get type, and allowed tools
            add edge ((y, x), T1) <-> ((y, x), T2) with weight=7

    """
    for y in range(regions.shape[0]):
        for x in range(regions.shape[1]):
            t1, t2 = allowed_tools[regions[y, x]]
            G.add_edge((y, x, t1), (y, x, t2), weight=7)

    """
    for each node in Graph
        extract_pos, T
        get possible neighbour positions up, down, left and right
        if neigbour with the same T exists add edge with weight=1

    """

    for y, x, t in G.nodes:
        # up
        if (y - 1, x, t) in G:
            G.add_edge((y, x, t), (y - 1, x, t), weight=1)
        # down
        if (y + 1, x, t) in G:
            G.add_edge((y, x, t), (y + 1, x, t), weight=1)
        # left
        if (y, x - 1, t) in G:
            G.add_edge((y, x, t), (y, x - 1, t), weight=1)
        # right
        if (y, x + 1, t) in G:
            G.add_edge((y, x, t), (y, x + 1, t), weight=1)
    """
    find shortest paths between ((0,0) T),  ((y, x), T)
    """
    return nx.shortest_path_length(G, (0, 0, 'T'), (ty, tx, 'T'), weight='weight')

if __name__ == '__main__':
    print(f'Part 1: {part_1().sum()}')
    print(f'Part 2: {part_2()}')