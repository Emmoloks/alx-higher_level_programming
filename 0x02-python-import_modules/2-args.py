#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    arg_str = "{} argument{}".format(argc, 's' if argc != 1 else '')

    if argc != 0:
        arg_str += ':'

    print(arg_str)

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
