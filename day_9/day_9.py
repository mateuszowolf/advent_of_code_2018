import re
from itertools import cycle
import time

datasets = []
with open('input.txt') as f:
    for line in f:
        data = tuple(int(x) for x in re.findall(r'\d+', line))
        datasets.append(data)


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def __repr__(self):
        l = self.left.value if self.left else None
        r = self.right.value if self.right else None
        return f"{self.value}-L:{l}-R:{r}"


def fuse(left, right):
    left.right = right
    right.left = left


def insert_marble(v, current):
    new = Node(v)
    immediate = current.right
    next_one = immediate.right
    fuse(immediate, new)
    fuse(new, next_one)
    return new


def pop_marble(marble):
    r = marble.right
    l = marble.left
    r.left = l
    l.right = r
    marble.right, marble.left = None, None
    return marble


def marbles_gen(last_marble):
    for i in range(1, last_marble+1):
        yield i

def play(circle, marbles, scores):
    current = circle
    players = cycle(list(scores.keys()))
    while True:
        current_player = next(players)
        try:
            marble = next(marbles)
        except StopIteration:
            return scores
        if marble % 23 == 0:
            scores[current_player] += marble
            c = current
            for i in range(7):
                c = c.left
            current = c.right
            scores[current_player] += pop_marble(c).value
        else:
             current = insert_marble(marble, current)


def part_1():
    players, last_marble = data
    scores = {i: 0 for i in range(1, players + 1)}
    marbles = marbles_gen(last_marble)
    start = Node(0)
    start.left, start.right = start, start
    scores = play(start, marbles, scores)
    print(max(scores.values()))


def part_2():
    players, last_marble = data
    last_marble *= 100
    scores = {i: 0 for i in range(1, players + 1)}
    marbles = marbles_gen(last_marble)
    start = Node(0)
    start.left, start.right = start, start
    scores = play(start, marbles, scores)
    print(max(scores.values()))

if __name__ == '__main__':
    mode = input('test/real\n')
    if mode.lower() in ('t', 'test'):
        data = datasets[0]
    else:
        data = datasets[1]

    stt = time.time()
    part_1()
    part_2()
    end = time.time()
    print(end-stt)

