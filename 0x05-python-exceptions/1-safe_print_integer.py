#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == int(value):
            print("{:d}".format(value))
            return True
        else:
            return False
    except ValueError:
        return False
