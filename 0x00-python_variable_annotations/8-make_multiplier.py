#!/usr/bin/env python3
"""
simple module that contains an annotated function returning
another function
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    the main function
    """
    def inside(multiplier: float) -> float:
        """
        the inner fynction that is being returned
        """
        return multiplier**2
    try:
        return inside
    except TypeError:
        print("multiplier must be a float value")
