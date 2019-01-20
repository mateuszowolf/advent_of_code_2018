import networkx as nx


def read_input():
    with open('input.txt') as f:
        inp = f.read()[1:-1]
    return inp

def parse_input():
    G = nx.Graph()
    direct = {'N': 1j, 'S': -1j, 'W': -1, 'E': 1}
    pos = 0
    queue = []

    inp = read_input()
    for char in inp:
        if char in direct:
            G.add_edge(pos, pos + direct[char])
            pos += direct[char]
        elif char == '(':
            queue.append(pos)
        elif char == ')':
            pos = queue.pop()
        elif char == '|':
            pos = queue[-1]
        else:
            raise Exception(f'Unexpected Character {char}')

    return G, 0

def part_1():
    G, start_pos = parse_input()
    return max(nx.single_source_shortest_path_length(G, start_pos).values())

def part_2():
    G, start_pos = parse_input()
    x = [l >= 1000 for l in nx.single_source_shortest_path_length(G, start_pos).values()]
    # x = list(nx.single_source_shortest_path_length(G, start_pos).values())
    return sum(x)


if __name__ == '__main__':
    print(part_1())
    print(part_2())