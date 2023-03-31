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
    source = input().strip()
    if source[0:1] == "I":
        pattern = input()
        text = input()
    elif source[0] == "F":
        filename = input().strip()
        if filename.endswith(".a"):
            print("Invalid file name")
            sys.exit()

        with open(filename, "r") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()

    matches = rabin_karp(pattern, text)
    print(" ".join(map(str, matches)))


if __name__ == "__main__":
    main()
