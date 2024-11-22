#!/bin/python3
import argparse

# import common
import three.perfectly_spherical_houses_in_a_vacuum as three

# from common import common


def main():
    parser = argparse.ArgumentParser(
        prog="advent_of_code",
        description="fun code problems",
    )

    parser.add_argument(
        "-d", "--day", type=str, required=True, help="The day of code to run"
    )

    args = parser.parse_args()

    match args.day:
        case "3" | "three":
            three.main()


if __name__ == "__main__":
    main()
