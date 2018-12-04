import numpy as np
import os
import re

FILE_PATH = os.path.join('day_3', 'input.txt')

with open(FILE_PATH) as f:
    claims = []
    for r in f.readlines():
        r = re.split('[^0-9]+', r[1:].strip())
        claims.append([int(d) for d in r])

fabric = np.zeros((1000,1000))

def part_1():

    for claim in claims:
        id, x, y, width, height = claim
        fabric[x:x+width, y:y+height] += 1
    print(len(fabric[fabric>1]))

def part_2():
    for claim in claims:
        id, x, y, width, height = claim
        if np.all(fabric[x:x+width, y:y+height] == 1):
            print(id)

if __name__ == '__main__':
        part_1()
        part_2()