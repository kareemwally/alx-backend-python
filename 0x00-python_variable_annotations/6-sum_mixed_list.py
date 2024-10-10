#!/usr/bin/python3
"""
simple module to define function
summing a list of float & int numbers
"""


from typing import List, Union, Optional


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ input_list is a list of float & int numbers
    and the result must be float"""
    try:
        return sum(mxd_lst)
    except TypeError:
        print("input_list must be an array of float/int")
