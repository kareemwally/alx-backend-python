#!/usr/bin/env python3
"""
module contains an annotated function taht returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ the 1st arg must be a str type
    and the 2nd must be either a float or int
    """
    try:
        return (k, v**2)
    except TypeError:
        print("v must be an int or float typed")
