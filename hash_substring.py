#!/usr/bin/env python3

import sys


def rabin_karp(pattern: str, text: str) -> list[int]:
    hpattern = hash(pattern)
    for i in range(len(text) - len(pattern) + 1):
        if hash(text[i : i + len(pattern)]) == hpattern:
            if text[i : i + len(pattern)] == pattern:
                yield i


def main():
    # I - input from keyboard
    # F - input from file
    mode = input().strip().upper()
    match mode:
        case "I":
            pattern = input()
            text = input()
        case "F":
            filename = input()
            if filename.endswith(".a"):
                print("Invalid file name")
                sys.exit(1)

            with open(filename, "r") as f:
                pattern = f.readline().strip()
                text = f.readline().strip()
        case _:
            print("Invalid input mode")
            sys.exit(1)

    matches = rabin_karp(pattern, text)
    print(" ".join(map(str, matches)))


if __name__ == "__main__":
    main()
