#!/usr/bin/python

from functions import *


def decode_grid_simple(grid, text):
    result = ""

    # split into squares divided by empty line
    for square in text.split("\n\n")[:-1]:
        for y in range(len(grid)):
            for x in grid[y]:
                result += square.split("\n")[y][x]

    return result


def encode_grid_simple(grid, text):
    result = ""

    char = 0
    while char < (len(text)):
        for y in range(len(grid)):
            for x in range(len(grid)):
                if x in grid[y]:
                    result += text[char]
                    if char == len(text) - 1:
                        xtmp = x
                        while xtmp < len(grid):
                            result += get_random_char()
                            xtmp += 1
                        return result
                    char += 1
                else:
                    result += get_random_char()
            result += "\n"
            if y == len(grid) - 1:
                result += "\n"

    return result
