#!/usr/bin/python3
"""Module to read from files."""


def read_file(filename=""):
    """Show the content of the file in stdout."""
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read(), end='')
