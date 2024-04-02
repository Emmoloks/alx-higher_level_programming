#!/usr/bin/python3
import sys
import hidden_4 as hidden_module

if __name__ == "__main__":
    for name in dir(hidden_module):
        if not name.startswith("__"):
            print(name)
