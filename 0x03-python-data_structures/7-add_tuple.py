#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()

    tuple_one = tuple_a + (0, 0)
    tuple_two = tuple_b + (0, 0)
    new_tuple = tuple_one[0] + tuple_two[0], tuple_one[1] + tuple_two[1]
    return new_tuple
