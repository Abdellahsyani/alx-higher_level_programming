#!/usr/bin/python3
alphabet = ""
for i in range(97, 123):
    quit = chr(i)
    if quit == 'e' or quit == 'q':
        continue
    alphabet += "{:s}".format(chr(i))
print(alphabet, end="")
