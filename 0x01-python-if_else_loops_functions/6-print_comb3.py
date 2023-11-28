#!/usr/bin/python3
for i in range(9):
    for j in range(i, 10):
        print("{:02d}".format(i * 10 + j), end=", " if j < 9 else "\n")
