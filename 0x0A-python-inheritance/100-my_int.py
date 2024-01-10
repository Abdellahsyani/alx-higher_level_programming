#!/usr/bin/python3
"""Troll Module use it to make your friend tilt."""


class MyInt(int):
    """An inting int."""

    def __eq__(self, other):
        """Is self equals other?"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Isn't self equals other?"""
        return super().__eq__(other)
