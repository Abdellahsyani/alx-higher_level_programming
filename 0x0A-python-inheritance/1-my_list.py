#!/usr/bin/python3
"""Module of the advanced list object."""


class MyList(list):
    """Make a new advanced list object."""
    def print_sorted(self):
        """Print the list in ascending sort."""
        print(sorted(self))
