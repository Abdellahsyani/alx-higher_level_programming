#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total_sum = 0

    for i in range(len(sys.argv)- 1):
        total_sum += int(sys.argv[i + 1])
    print("{}".format(total_sum))
