#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    result = 0
    for i in my_list:
        if i not in new_set:
            new_set.add(i)
            result += i
    return result
