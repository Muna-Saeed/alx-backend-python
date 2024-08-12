#!/usr/bin/env python3
"""6. Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ the sum_mixed_list function with type annotations for
    a list containing both integers and floats"""
    return float(sum(mxd_lst))
