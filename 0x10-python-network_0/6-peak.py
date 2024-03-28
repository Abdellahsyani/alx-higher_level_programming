#!/usr/bin/python3
"""find the peak number"""


def find_peak(list_of_integers):
    """Yes, I'm the one who will find it"""
    if type(list_of_integers) is not list:
        return None
    if len(list_of_integers) == 0:
        return None

    prev = list_of_integers[0]
    dir_was = 0
    dir_is = 0
    for i in list_of_integers[1:]:
        dir_was = dir_is
        dir_is = i - prev
        if dir_is < 0 and dir_was > 0:
            return prev
        prev = i

    if dir_is > 0:
        return prev
    return list_of_integers[0]
