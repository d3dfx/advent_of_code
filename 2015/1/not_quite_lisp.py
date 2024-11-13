#!/bin/python3

year = 2015
day = 1


def main():
    santa_loc = 0
    puzzle_input = get_puzzle_input()
    trip = True

    for idx in range(len(puzzle_input)):
        char = puzzle_input[idx]
        print("santa's location: " + str(santa_loc))
        if char == "(":
            santa_loc = up_one_floor(santa_loc)
        elif char == ")":
            santa_loc = down_one_floor(santa_loc)
            if santa_loc == -1 and trip:
                first_basement_dir = idx + 1
                trip = False
        else:
            continue

    print("Santa End Loc: " + str(santa_loc))
    print("First Direction to Enter Basement: " + str(first_basement_dir))


def up_one_floor(num):
    return num + 1


def down_one_floor(num):
    return num - 1


def get_puzzle_input():
    with open("./puzzle_input.txt") as puzzle_input:
        return puzzle_input.read()


if __name__ == "__main__":
    main()
