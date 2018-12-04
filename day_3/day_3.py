import numpy as np
import os

FILE_PATH = os.path.join('day_3', 'input.txt')

def part_1():
    fabric = np.zeros((1000,1000))

    with open(FILE_PATH, 'r') as f:
        for claim in f:
            # claim = "#1 @ 1,3: 4x5\n"
            claim = claim.strip().split()
            x, y = claim[2].strip(':').split(',')
            x, y = int(x), int(y)
            width, height = claim[3].split('x')
            width, height = int(width), int(height)

            for row in range(y, y+height):
                for column in range(x, x+ width):
                    fabric[row][column] += 1

    print(len(fabric[fabric>1]))

if __name__ == '__main__':
    choice = int(input('Which part woud you like to run: \n'))
    if choice == 1:
        part_1()
    # elif choice == 2:
    #     part_2()
    else:
        print('only 1 or 2 are covered')