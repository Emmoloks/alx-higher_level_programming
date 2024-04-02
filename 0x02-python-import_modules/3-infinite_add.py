#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    index = 0
    total = 0
    for arg in sys.argv:
        if index != 0:
            total += int(arg)
        else:
            index += 1

    print("{:d}".format(total))
