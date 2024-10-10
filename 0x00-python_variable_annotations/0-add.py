#!/usr/bin/env python3
"""
simple module that contains a type-checked function
"""


def add(a: float, b: float) -> float:
    """ adding two float arguments a,b"""
    try:
        return a+b
    except TypeError:
        print("a & b must be floats")
        return None
