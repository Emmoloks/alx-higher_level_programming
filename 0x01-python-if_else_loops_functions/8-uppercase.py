#!/usr/bin/python3
def uppercase(string):
    uppercase_string = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    print("{}".format(uppercase_string))
