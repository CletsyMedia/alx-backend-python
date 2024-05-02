#!/usr/bin/env python3
"""
Module for sum_mixed_list function
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the list of int and float
    """
    return sum(mxd_lst)
