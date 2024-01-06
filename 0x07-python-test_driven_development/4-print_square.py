#!/usr/bin/python3
'''Define a function to print square area'''


def print_square(size):
    '''function that print a square with #
    Args:
        size(int): the size of square
        Return: the square area of size
    Raises:
        TypeError: if The size is not integer
        ValueError: if The size is less that 0
        TypeError: if The size is float and less than 0
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#'*size)
