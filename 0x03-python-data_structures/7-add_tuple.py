#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    a_len = len(tuple_a)
    b_len = len(tuple_b)
    new_tup = ()
    for i in range(2):
        if i >= a_len:
            val_a = 0
        else:
            val_a = tuple_a[i]
        if i >= b_len:
            val_b = 0
        else:
            val_b = tuple_b[i]

        if (i == 0):
            new_tup = (val_a + val_b,)
        else:
            new_tup += (val_a + val_b,)

    return new_tup
