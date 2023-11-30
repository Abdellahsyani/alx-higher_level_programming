#!/usr/bin/python3
import sys
sys.argv
num_args = len(sys.argv)

if num_args == 0:
    print("{} arguments.".format(0))
if num_args > 0:
    print("{} argument:".format(num_args))
if num_args > 0:
    for i in range(num_args):
        print("{}: {}".format(i, sys.argv[i]))
        i + 1
