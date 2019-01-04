import logging
from collections import deque
import time
from colorama import init
init()

class Unit:

    def __init__(self, unit_type, x, y, hp, ap):
        self.type = unit_type
        self.x = x
        self.y = y
        self.hp = hp
        self.initial_hp = hp
        self.ap = ap

    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y and self.x < other.x:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.type.upper()[0]} {self.position()} {self.hp}/{self.initial_hp}"

    def is_alive(self):
        return self.hp > 0

    def take_hit(self, attack):
        self.hp -= attack
        return self.is_alive()

    def position(self):
        return tuple([self.x, self.y])

    def move(self, new_x, new_y):
        # dist = self.move_dist(self.x, self.y, new_x, new_y)
        # print(self.type, self.position() , (new_x, new_y))
        self.x = new_x
        self.y = new_y
        return True

    def move_dist(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def find_nearest_target(self, map_, excluded_fields, targets):
        """
        map
        self.position as starting point
        excluded fields - fields that are in map but are not accessible
        targets - fields to which paths need to be found
        this finds the closes target but doesn't give you the first step you should take
        """
        queue = deque()
        queue.append([self.position()])
        visited = set()
        while queue:
            cur_path = queue.popleft()
            cur = cur_path[-1]
            if cur in targets:
                return cur_path
            elif cur in visited:
                continue
            else:
                visited.add(cur)

                queue.extend([cur_path + [f] for f in get_neighbours(*cur) if f in map_ and f not in
                              excluded_fields])
        return []


def get_neighbours(x, y):
    return [(x, y-1),(x-1, y), (x+1, y), (x, y+1)]


class GameEndException(Exception):
    pass


class Game:
    height = 0
    width = 0

    def setup(self, file_name='input.txt', elf_ap=3):
        """
        parse the input
        get map
        create all units
        :return:
        """
        map_ = []
        units = []
        with open(file_name, 'r') as f:
            data = [list(line.strip()) for line in f]
        Game.height = len(data)
        Game.width = len(data[0])

        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] in "EG":
                    if data[y][x] == 'G':
                        ap = 3
                    else:
                        ap = elf_ap
                    units.append(Unit(data[y][x], x, y, 200, ap))
                    data[y][x] = '.'

        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == '.':
                    map_.append((x, y))

        return map_, units

    def play_round(self, map_, units):
        """
        sort units
        for each unit:
            if not alive, continue, unit is no longer in play
            identify remaining alive targets
            if no targets alive raise GameEndException
            for each remaining target - get neighbouring fields - target fields to try to move to
            for each unit other than yourself - get position - excluded fields to be removed from map
            using bfs with start, target fields, map and excluded fields, find path to nearest target
            if path is available: move to first step

            attack
            get neighbouring positions
            check for any enemies in neigbouring positions
            sort targets by lowest hitpoint first, reading order
            if at least one target available, hit with ap
            if len of targets is 1 and result of hit is kill raise GameEndException
        :return:
        """
        units.sort()
        for character in units:
            if not character.is_alive():
                continue

            targets = [u for u in units if u.is_alive() and u.type != character.type]
            # print(targets)
            if not targets:
                # print(130)
                raise GameEndException

            target_fields = []
            for target in targets:
                target_fields.extend(get_neighbours(*target.position()))

            excluded_fields = [u.position() for u in units if u is not character and u.is_alive()]
            path = character.find_nearest_target(map_, excluded_fields, target_fields)
            if len(path) > 1: # there's at least one step after current position
                character.move(*path[1])

            targets_in_range = [u for u in targets if u.position() in get_neighbours(*character.position())]
            if targets_in_range:
                attack_target = sorted(targets_in_range, key=lambda c: (c.hp, c))[0]
                still_alive = attack_target.take_hit(character.ap)
                # if len(targets) == 1 and not still_alive:
                #     # print(f"after {attack_target}")
                #     # print(targets)
                #     # print('146')
                #     raise GameEndException
        return sorted(units)

    def play_game(self, elf_ap=3):
        """
        invoke setup to generate map and units
        create round counter
        while True
            try:
            play round
            increment counter
            :except GameEndException
            log units, log info on which group won

        return counter of rounds, sum of health
        :return:
        """
        map_, units = self.setup(elf_ap=elf_ap)
        elf_roster = "".join([u.type for u in units if u.type == 'E'])
        counter = 0
        # print(f"{counter} {units}")
        # self.print_status(map_, units)
        while True:
            try:
                self.play_round(map_, units)
                counter += 1
                # print(f"{counter} {units}")
                # self.print_status(map_, units)
                time.sleep(0.2)
            except GameEndException:
                # self.print_status(map_, units)
                units_alive = [u for u in units if u.is_alive()]
                hp_sum = sum(u.hp for u in units_alive)
                winning_group = "".join([u.type for u in units_alive])
                return counter, hp_sum, winning_group, elf_roster

    def print_status(self, map_, units):
        status = {True: color.GREEN, False: color.RED}
        units = sorted(units.copy())
        # print(units)
        positions = {u.position(): u for u in units}
        for y in range(Game.height):
            for x in range(Game.width):
                c_to_print = " "
                if (x, y) in positions:
                    u = positions[(x, y)]
                    c_to_print = status[u.is_alive()] + u.type + color.END
                elif (x, y) in map_:
                    c_to_print = '.'
                else:
                    c_to_print = '#'

                print(c_to_print, end="")
            print()




class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

if __name__ == '__main__':
    g = Game()
    # part 1
    # counter, hp_sum, winning_group, _ = g.play_game()
    # part 2
    elf_ap = 4
    while True:
        counter, hp_sum, winning_group, elf_roster = g.play_game(elf_ap)
        if winning_group == elf_roster:
            print(elf_ap)
            break
        else:
            elf_ap+=1
            print(elf_ap)
    print(winning_group)
    print((counter, hp_sum))
    print(counter*hp_sum)


