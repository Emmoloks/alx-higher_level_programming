#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    char_first = sentence[0]
    if sentence:
        return(str_len, char_first)
    else:
        return(0, None)