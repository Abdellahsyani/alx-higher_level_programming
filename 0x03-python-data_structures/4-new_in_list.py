#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list.copy()
    else:
        if my_list:
            my_list.copy()
            my_list[idx] = element
            print("{:d}".format(my_list[idx]))
