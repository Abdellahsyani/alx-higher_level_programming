#!/usr/bin/python3
"""Module to save strings into files."""


def write_file(filename="", text=""):
    """Write some text to a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
