#!/usr/bin/python3
"""Module to save strings into files."""


def append_write(filename="", text=""):
    """Append some text to a file."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
