#!/bin/python3
import itertools
from os import path

from common import common
from more_itertools import pairwise, windowed


def main(part="1"):
    txt = common.get_puzzle_input(path.dirname(__file__) + "/puzzle_input.txt")
    txt = txt.strip().split("\n")

    if part == "1":
        ans = part_1(txt)
    else:
        ans = part_2(txt)

    print(f"Part {part} Answer: {ans}")


def part_1(puzzle_input):
    nice_string = []
    for string in puzzle_input:

        three_vowels = False
        consecutive_char = False

        if (
            string.find("ab") >= 0
            or string.find("cd") >= 0
            or string.find("pq") >= 0
            or string.find("xy") >= 0
        ):
            continue
        else:
            vowels = ("a", "e", "i", "o", "u")
            vowel_count = 0
            register = ""
            for char in string:
                if register == char and not consecutive_char:
                    consecutive_char = True

                if char in vowels and not three_vowels:
                    vowel_count += 1

                    if vowel_count >= 3:
                        three_vowels = True

                if three_vowels and consecutive_char:
                    nice_string.append(string)
                    break

                register = char
    return str(len(nice_string))


def part_2(puzzle_input):
    nice_string = []
    for string in puzzle_input:

        double_pair = False
        alternating_pair = False

        pair_map = {}
        pair_idx_tracker = []
        register = ("", "", "")
        idx = 0
        str_len = len(string)
        while register != (string[-1], "", ""):
            if idx >= str_len:
                register = (register[1], register[2], "")
                continue
            else:
                char = string[idx]
                register = (register[1], register[2], char)

            map_key = f"{register[1]}{char}"
            if map_key == char * 2:
                if idx - 1 not in pair_idx_tracker:
                    pair_idx_tracker.append(idx)
                    pair_map[map_key] = pair_map.get(map_key, 0) + 1

                    if pair_map[map_key] >= 2:
                        double_pair = True
            else:
                pair_map[map_key] = pair_map.get(map_key, 0) + 1
                if pair_map[map_key] >= 2:
                    double_pair = True

            if register[0] == char:
                alternating_pair = True

            if double_pair and alternating_pair:
                nice_string.append(string)
                break

            idx += 1
    return str(len(nice_string))


if __name__ == "__main__":
    main()
