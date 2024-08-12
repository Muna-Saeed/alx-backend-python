#!/usr/bin/env python3
"""12. Type Checking"""
from typing import List, Tuple, Union


def zoom_array(
        lst: List[Union[int, float]], factor: int = 2
        ) -> List[Union[int, float]]:
    """
    Zooms in on the elements of a list by a given factor.

    Parameters:
    lst (List[Union[int, float]]): A list of integers or floats.
    factor (int): The number of times to repeat each element. Defaults to 2.

    Returns:
    List[Union[int, float]]: A list with elements
    repeated according to the factor.

    Example:
    >>> zoom_array([12, 72, 91])
    [12, 12, 72, 72, 91, 91]
    >>> zoom_array([12, 72, 91], 3)
    [12, 12, 12, 72, 72, 72, 91, 91, 91]
    """
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

# Correctly pass an integer factor
zoom_3x = zoom_array(array, 3)
