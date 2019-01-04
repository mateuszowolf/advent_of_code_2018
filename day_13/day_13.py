import numpy as np
from itertools import cycle
"""
carts running on tracks
originally carts marked by position and their direction <>^v
when arriving on intersections cars turn left, straight, right, left, straight ...

movement - all carts move once per round, 
carts move in order from top to bottom and from left to right
if at any point carts occupy the same space, a crash occurs (even if not all carts have moved yet in this round)

tracks consist of straight paths - vertical (|) horizontal (-)
turns - (\ & /) and intersections + carts can turn left, right or continue straight
empty fields/spaces - outside of lines

top left - (x:0, y:0)
goal: identify site of first crash (x, y)
"""


class Cart:

    direction_identifiers = ('^', 'v', '>', '<')

    def __init__(self, posX, posY, dir_char):
        self.posX = posX
        self.posY = posY
        self.dire = self.set_direction(dir_char)
        self.intsect_turns = cycle(['left', 'straight', 'right'])

    def __repr__(self):
        return f'{self.posX},{self.posY}-{self.dire}'

    def set_direction(self, dir_char):
        if dir_char == '^':
            return 'up'
        if dir_char == 'v':
            return 'down'
        if dir_char == '>':
            return 'right'
        if dir_char == '<':
            return 'left'
        raise ValueError(f'unexpected direction character {dir_char}')

    def __lt__(self, other):
        if self.posY < other.posY:
            return True
        elif self.posY == other.posY and self.posX < other.posX:
            return True
        return False

    def __eq__(self, other):
        if self.posY == other.posY and self.posX == other.posX:
            return True
        return False

    def intersection(self):
        for d in self.intsect_turns:
            return d

    def move(self):
        if self.dire == 'up':
            self.posY -= 1
        elif self.dire == 'down':
            self.posY += 1
        elif self.dire == 'left':
            self.posX -= 1
        elif self.dire == 'right':
            self.posX += 1
        else:
            raise NotImplementedError('something wrong')

    def get_position(self):
        return (self.posX, self.posY)

    def change_direction(self, track):
        if track in ('-', '|'):
            return
        elif track in ('\\', '/'):
            if self.dire == 'up':
                self.dire = 'left' if track == '\\' else 'right'
            elif self.dire == 'left':
                self.dire = 'up' if track =='\\' else 'down'
            elif self.dire == 'down':
                self.dire = 'right' if track == '\\' else 'left'
            else:
                self.dire = 'down' if track == '\\' else 'up'
            return
        elif track == '+':
            self.dire = self.get_new_dire()
        else:
            raise NotImplementedError(f'Unrecognised track {track}')

    def get_new_dire(self):
        i = self.intersection()
        if i == 'straight':
            return self.dire
        if i == 'left':
            if self.dire == 'up':
                return 'left'
            elif self.dire == 'left':
                return 'down'
            elif self.dire == 'down':
                return 'right'
            else:
                return 'up'
        if i == 'right':
            if self.dire == 'up':
                return 'right'
            elif self.dire == 'left':
                return 'up'
            elif self.dire == 'down':
                return 'left'
            else:
                return 'down'




def load_map():
    carts = []
    with open('input.txt', 'r') as f:
        tracks = [line.strip('\n') for line in f]
    max_l = max([len(l) for l in tracks])
    tracks = [list(l.ljust(max_l, ' ')) for l in tracks]
    tracks = np.array(tracks)
    for y in range(0, tracks.shape[0]):
        for x in range(0, tracks.shape[1]):
            if tracks[y, x] in Cart.direction_identifiers:
                carts.append(Cart(posX=x, posY=y, dir_char=tracks[y, x]))
                tracks[y, x] = get_track(tracks=tracks, x=x, y=y, char=tracks[y, x])
    return carts, tracks


def get_track(tracks, x, y, char):
    if y == 0: # can't go above 0
        return '-'
    if x == 0: # can't go further left
        return '|'
    if tracks[y, x-1] == ' ' or tracks[y, x+1] == ' ':
        return '|'
    if tracks[y, x-1] == '-' or tracks[y, x+1] == '-':
        return '-'
    if tracks[y-1, x] == ' ' or tracks[y+1, x] == ' ':
        return '-'
    if tracks[y-1, x] == '|' or tracks[y+1, x] == '|':
        return '|'
    raise NotImplementedError(f'not solved {char}')

def main_p1():
    carts, map = load_map()
    ticks = 0
    while True:
        """
        print ticks if divisible by 100
        sort carts to get them in order they'll be moving in
        get positions
        for cart in carts:
            remove current position from positions
            tick - move one position, check track underneath,
                if necessary (turn or intersection) change direction of the cart)
                get new position, if it already exists in positions, print it out as collision position and raise exception,
                otherwise add new pos to positions
        increment ticks
        """
        if ticks % 100 == 0:
            print(ticks)
        carts.sort()
        positions = set(c.get_position() for c in carts)
        for c in carts:
            positions.remove(c.get_position())
            c.move()
            n_pos = c.get_position()
            c.change_direction(map[n_pos[1], n_pos[0]])
            if n_pos in positions:
                print(f'Crash at {n_pos}')
                raise Exception(f'Crash at {n_pos}')
            else:
                positions.add(n_pos)
        ticks += 1

def main_p2():
    carts, map = load_map()
    ticks = 0
    while True:
        """
                print ticks if divisible by 100
                sort carts to get them in order they'll be moving in
                get positions
                make a shallow copy of carts
                for cart in carts_copy:
                    remove current position from positions
                    tick - move one position, check track underneath,
                        if necessary (turn or intersection) change direction of the cart)
                        get new position, if it already exists in positions
                        if pos in positions:
                            to_remove = [c for c in carts if c==current and current is not c]
                        for c in to_remove:
                            carts.remove(c)

                if len(carts) = 1:
                    print(carts[0])
                increment ticks
                """
        if ticks % 100 == 0:
            print(ticks)
        positions = set(c.get_position() for c in carts)
        carts_copy = carts.copy()
        to_remove = []
        for c in carts:
            if c in to_remove:
                continue
            positions.remove(c.get_position())
            c.move()
            n_pos = c.get_position()
            c.change_direction(map[n_pos[1], n_pos[0]])
            if n_pos in positions:
                to_remove.extend([cart for cart in carts if cart == c and cart is not c] +[c])
            else:
                positions.add(n_pos)
        for cart in to_remove:
            carts.remove(cart)
        if len(carts) ==1:
            print(carts[0])
            break
        print(carts)
        ticks += 1


if __name__ == '__main__':
    #main_p1()
    main_p2()