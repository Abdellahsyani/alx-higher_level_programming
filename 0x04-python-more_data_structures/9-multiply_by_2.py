#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = sorted(a_dictionary)
    for key in new_dictionary:
        print("{}: {}".format(key, a_dictionary[key] * 2))
