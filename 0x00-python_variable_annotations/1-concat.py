#!/usr/bin/env python3
"""
simple module that contains a type-checked function
"""


def concat(str1: str, str2: str) -> str:
    """ concatening two strings arguments str1, str2"""
    try:
        return str1 + str2
    except TypeError:
        print("str1 & str2 must be strings")
        return None
