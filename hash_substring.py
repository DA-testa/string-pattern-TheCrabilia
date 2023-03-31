#!/usr/bin/env python3

import sys


def rabin_karp(pattern: str, text: str) -> list[int]:
    hpattern = hash(pattern)
    for i in range(len(text) - len(pattern) + 1):
        if hash(text[i : i + len(pattern)]) == hpattern:
            if text[i : i + len(pattern)] == pattern:
                yield i


def main():
    mode = input().rstrip()
    if mode == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif mode == "F":
        with open("tests/06", "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        print("Invalid mode")
        sys.exit(1)

    matches = rabin_karp(pattern, text)
    print(list(matches))
    print(" ".join(map(str, matches)))


if __name__ == "__main__":
    main()
