#!/bin/python3
from math import prod

import common_advent as common


def main():
    puzzle_input = common.get_puzzle_input()
    puzzle_input = puzzle_input.strip().split("\n")

    ribbon_len_log = []
    sa_log = []
    for arg in puzzle_input:
        arg = arg.split("x")
        ribbon_len_log.append(get_ribbon_length(arg[0], arg[1], arg[2]))
        sa_log.append(get_present_surface_area(arg[0], arg[1], arg[2]))

    print("Wrapping Paper Needed in Feet:", sum(sa_log))
    print("Ribbon needed in Feet:", sum(ribbon_len_log))


def get_present_surface_area(length, width, height):
    side1 = int(length) * int(width)
    side2 = int(width) * int(height)
    side3 = int(height) * int(length)

    smallest_side = min(side1, side2, side3)
    return 2 * side1 + 2 * side2 + 2 * side3 + smallest_side


def get_ribbon_length(length, width, height):
    sort_sizes = [int(length), int(width), int(height)]
    # sort_sizes = sorted([int(length), int(width), int(height)])

    bow_length = prod(sort_sizes)

    bow_present_wrap = (2 * sort_sizes[0]) + (2 * sort_sizes[1])

    return bow_length + bow_present_wrap


if __name__ == "__main__":
    main()
