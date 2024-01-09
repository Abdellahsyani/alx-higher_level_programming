#!/usr/bin/python3
"""Module for representing Pascal's triangles."""


def pascal_triangle(n):
    """
    Get a list of lests of integers represents
    the Pascal's triangle of ``n``
    """
    triangle = []
    row = []
    old = [1]
    if n <= 0:
        return triangle
    for y in range(n):
        for x in range(y + 1):
            val = 1
            if 0 < x < y:
                val = old[x] + old[x - 1]
            row.append(val)
        triangle.append(row)
        del old
        old = row
        row = []
    return triangle
