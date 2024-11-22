#!/bin/python3
import hashlib
from os import path

from common import common


def main():
    key = common.get_puzzle_input(path.dirname(__file__) + "/puzzle_input.txt")
    key = key.strip()
    md5sum = ""
    ans = 0
    while md5sum[:6] != "000000":
        ans += 1
        puzzle_input = key + str(ans)
        md5sum = hashlib.md5(puzzle_input.encode()).hexdigest()

    print(f"Answer is {ans}")
    print(md5sum)


if __name__ == "__main__":
    main()
