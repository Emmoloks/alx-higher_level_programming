#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        reverse = my_list[0:]
        reverse.reverse()
        for i in range(len(reverse)):
            print("{:d}".format(reverse[i]))
