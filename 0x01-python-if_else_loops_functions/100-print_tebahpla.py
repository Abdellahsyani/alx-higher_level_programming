#!/usr/bin/python3
''' authur abdellah'''
for i in range(ord('z'), ord('A') - 1, -1):
    value = chr(i)

    if (i - ord('z')) % 2 == 0:
        value = value.lower()
    else:
        value = value.upper()
    print(value, end="")
