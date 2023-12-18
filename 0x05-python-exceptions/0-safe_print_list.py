#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print("{}".format(my_list))
        for i in my_list:
            x += 1
        print("{}".format(x))
    except ValueError:
        print("Oop's there is a problem")
