#!/usr/bin/python3
if __name__ == "__main__":
    '''splite the list'''
    import sys
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("{} arguments.".format(0))
    elif num_args == 1:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(num_args))
    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
