#!/bin/python3

from os import path

from common import common


def main():
    txt = common.get_puzzle_input(path.dirname(__file__) + "/puzzle_input.txt")
    santa_loc = (0, 0)
    robo_santa_loc = (0, 0)
    santa_loc_log = [(0, 0), (0, 0)]
    santa_turn = True

    for char in txt:
        if santa_turn:
            current_santa = santa_loc
        else:
            current_santa = robo_santa_loc

        if char == "^":
            current_santa = move_santa_north(current_santa)
        elif char == "v":
            current_santa = move_santa_south(current_santa)
        elif char == ">":
            current_santa = move_santa_east(current_santa)
        elif char == "<":
            current_santa = move_santa_west(current_santa)

        if santa_turn:
            santa_loc = current_santa
            santa_loc_log.append(santa_loc)
            santa_turn = False
        else:
            robo_santa_loc = current_santa
            santa_loc_log.append(robo_santa_loc)
            santa_turn = True

    unique_loc = set(santa_loc_log)
    print(f"Santa unique locations: {len(unique_loc)}")


def move_santa_north(loc):
    return (loc[0], loc[1] + 1)


def move_santa_south(loc):
    return (loc[0], loc[1] - 1)


def move_santa_east(loc):
    return (loc[0] + 1, loc[1])


def move_santa_west(loc):
    return (loc[0] - 1, loc[1])


if __name__ == "__main__":
    main()
