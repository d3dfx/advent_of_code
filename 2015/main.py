#!/bin/python3
import argparse

import five.doesnt_he_have_intern_elves_for_this as five
import four.the_ideal_stocking_stuffer as four
import three.perfectly_spherical_houses_in_a_vacuum as three


def main():
    parser = argparse.ArgumentParser(
        prog="advent_of_code",
        description="fun code problems",
    )

    parser.add_argument(
        "-d", "--day", type=str, required=True, help="The day of code to run"
    )
    parser.add_argument(
        "-p",
        "--part",
        type=str,
        help="The Part to execute",
        choices=["1", "2"],
        default="1",
    )

    args = parser.parse_args()

    match args.day:
        case "3" | "three":
            three.main()
        case "4" | "four":
            four.main()
        case "5" | "five":
            five.main(args.part)


if __name__ == "__main__":
    main()
