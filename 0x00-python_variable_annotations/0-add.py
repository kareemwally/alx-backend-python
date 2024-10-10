#!/usr/bin/python3
"""
simple module that contains a type-checked function
>>> add(3.4,5.0)
8.4
"""


def add(a: float, b: float) -> float:
    """ adding two float arguments a,b"""
    try:
        return a+b
    except TypeError:
        print("a & b must be floats")
        return None
