#!/usr/bin/env python3
"""
simple module that contains a type-checked function
>>> floor(3.14)
3
"""


def floor(n: float) -> int:
    """ getting the floor -int- value of a float-arg n"""
    try:
        return math.floor(n)
    except TypeError:
        print("n must be float")
        return None
