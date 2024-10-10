#!/usr/bin/env python3
"""
a module containing a function to return list of
tuples of two items(sequence, int)
"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function takes an itratable arg (sequence)
    and returning a list of tuples of two items(sequence, int)
    """
    return [(i, len(i)) for i in lst]
