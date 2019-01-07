import numpy as np
import re
import tempfile
import os
from collections import deque

pattern = re.compile('\d+')

def read_input():
    map_ = np.zeros((2050, 1000), dtype=str)
    map_[:,:] = '.'
    file = 'input.txt'
    # file = 'test_input.txt'
    with open(file) as f:
        for line in f:
            first, second = line.split(', ')
            ax, coord = first.split('=')
            start, end = list(map(int, re.findall(pattern, second)))
            if ax == 'y':
                map_[int(coord), start:end+1] = '#'
            else:
                map_[start:end+1, int(coord)] = '#'

    map_, top_y, source_shift = trim(map_)
    return map_, [Source(0, 500-source_shift)], top_y  #


class Source:

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x


    def mark(self, area, chr, pos=None):
        if not pos:
            pos = self.get_position()
        y, x = pos
        area[y, x] = chr

    def get_position(self):
        return (self.y, self.x)

    def spread(self, area, y, x):
        new_sources = []
        self.mark(area, '~', (y, x))
        right = self.spread_right(area, y, x)
        left = self.spread_left(area, y, x)
        if right:
            new_sources.append(right)
        if left:
            new_sources.append(left)
        return new_sources

    def spread_right(self,area, y, x):
        while True:
            if area[y, x+1] in ('.', '|', '~','+'):
                x += 1
                self.mark(area, '~', (y, x))
            else:
                return False
            if area[y+1, x] in ('.','|'):
                return Source(y, x)

    def spread_left(self,area, y, x):
        while True:
            if area[y, x-1] in ('.', '|', '~','+'):
                x -= 1
                self.mark(area, '~', (y, x))
            else:
                return False
            if area[y+1, x] in ('.','|'):
                return Source(y, x)

    def drip_down(self, area):
        """mark current position, continue the path downwards, when clay is hit, spread sideways or upwards to until
        overflow is encountered, return list of new sources
        if path traveling downwards ends up outside of area, return empty list
        """
        y, x = self.get_position()
        self.mark(area, '+', (y, x))

        while True:
            try:
                next = area[y+1, x]
                if next in ('.', '~'):
                    y += 1
                else: break;
            except IndexError:
                return []
            self.mark(area, '|', (y, x))

        overflows = []
        i=0
        while len(overflows) == 0:
            overflows = self.spread(area, y, x)
            # print(len(overflows))
            if len(overflows) == 0:
                # print(overflows)
                y -= 1
                self.mark(area, '~', (y, x))
                # i +=1
        # overflows = self.spread(area, y, x)

        return overflows





def trim(area):
    y = [y for y in range(area.shape[0]) if '#' in area[y,:]]
    max_y = max(y)
    min_y = min(y)

    x = [x for x in range(area.shape[1]) if '#' in area[:, x]]
    max_x = max(x)
    min_x = min(x)

    trimmed = area[:max_y+1, min_x-1:max_x+2]
    return trimmed, min_y, min_x-1


def visualise(area):
    # area[area == '.'] = chr(11035)
    # area[area == '#'] = 'X'
    # area[area == '+'] = '+'

    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
        for line in area:
            f.write("""
                <!DOCTYPE html>
                 <meta charset="UTF-8"> 
    <html>
    <body><p style="font-family:Courier; padding:0; margin:0; line-height : 20px; font-size:20px;letter-spacing:0px">""")
            f.write("".join(line))
        f.write("</p></body></html>")
        name = f.name
    os.popen(f'start {name}')

def part_1():
    area, sources, top_y = read_input()
    sources = deque(sources)
    seen_sources = []
    count = 0
    while sources:
        source = sources.popleft()
        count +=1

        try:
            new_sources = source.drip_down(area)
            for s in new_sources:
                if s not in sources and s not in seen_sources:
                    sources.append(s)
                    seen_sources.append(s)
        except IndexError:
            visualise(area)
            raise

        # if count > 30:
        #     visualise(area)
        #     raise Exception

    # print(area[0])

    countable_area = area[top_y:,:]
    visualise(countable_area)
    flowing = (countable_area == '|').sum()
    standing = (countable_area == '~').sum()
    sources = (countable_area == '+').sum()
    return print(flowing + standing + sources)


if __name__ == '__main__':
    print(part_1())

