#!/usr/bin/python3
"""
simple module to define function
summing a list of float numbers
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ input_list is a list of floats and the result must be float"""
    try:
        return sum(input_list)
    except TypeError:
        print("input_list must be an array of floats")
