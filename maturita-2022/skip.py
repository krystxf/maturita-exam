#!/usr/bin/python

from functions import *


def decode_skip(skip, offset, encoded):
    # offset & skip
    return encoded[offset:-1:skip + 1]


def encode_skip(skip, offset, text):
    result = ""

    for _ in range(offset):
        result += get_random_char()

    for char in text:
        result += char
        for _ in range(skip):
            result += get_random_char()

    return result
