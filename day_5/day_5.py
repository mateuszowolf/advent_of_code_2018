from string import ascii_lowercase, ascii_uppercase
from collections import defaultdict
import re
import time
import datetime

LETTERS_MAPPING = x = {**{u: l for u, l in zip(ascii_uppercase, ascii_lowercase)},
                       **{l: u for l, u in zip(ascii_lowercase, ascii_uppercase)}}


def get_input():
    with open('day_5/input.txt', 'r') as file:
        text = file.read().strip()
    return text

def collapse(s):
    start = 1
    while True:
        changed = False
        for i in range(start, len(s)):
            if s[i-1] == LETTERS_MAPPING[s[i]]:
                new_string = s[:i-1] + s[i+1:]
                s = new_string
                changed = True
                start = max(i-3, 1)
                break

        if not changed:
            break
    return s

def part_1():
    s = get_input()
    s = collapse(s)
    print(len(s))

def part_2():
    original_string = get_input()
    results = defaultdict(list)
    for letter in ascii_uppercase:
        print(letter)
        letter_removed = re.sub(letter, "", original_string, flags=re.IGNORECASE)
        results[len(collapse(letter_removed))].append(letter)

    m = min(results.keys())
    print(f"{m} {results.get(m)}")


if __name__ == "__main__":
    stt = datetime.datetime.now()
    part_1()
    part_2()
    print(datetime.datetime.now() - stt)