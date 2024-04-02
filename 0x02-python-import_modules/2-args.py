#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    arg_format = "{} argument"
    if num_args == 0:
        arg_format += 's.'
    elif num_args == 1:
        arg_format += ':'
    else:
        arg_format += 's:'

    print(arg_format.format(num_args))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

