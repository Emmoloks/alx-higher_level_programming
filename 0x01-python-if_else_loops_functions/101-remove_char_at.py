#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0:
        return (s)
    return (s[:n] + s[n + 1:])
