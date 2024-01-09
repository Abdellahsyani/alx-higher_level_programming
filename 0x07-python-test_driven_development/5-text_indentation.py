#!/usr/bin/python3
"""Genius tools for printing squares."""


def print_square(size):
    """
    Print a square using the character '#'.

    Args
    ----
    size: int, non negative number
        The lenght of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    row = '#' * size + '\n'
    print(row * size, end='')
