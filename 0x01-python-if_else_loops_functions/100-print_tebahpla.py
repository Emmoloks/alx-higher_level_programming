#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i)), end="")
    i -= 1
    if i >= ord('a'):
        print("{}".format(chr(i).upper()), end="")
