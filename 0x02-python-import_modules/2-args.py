#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    arg_list = argv[1:]

    if num_args != 1:
        print("{} argument{}:".format(num_args, 's'))
    else:
        print('', end="")
        if num_args == 0:
            print("{}".format("."))
        else:
            print("")

            for i, arg in enumerate(arg_list, start=1):
                print("{}: {}".format(i, arg))
