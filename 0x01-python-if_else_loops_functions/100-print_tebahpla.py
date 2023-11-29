#!/usr/bin/python3
''' authur abdellah'''
value = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i + value)), end="")
    value = 32 if i == 0 else 0
