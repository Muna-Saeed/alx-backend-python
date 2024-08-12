#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it is not empty,
    otherwise returns None.

    Parameters:
    lst (Sequence[Any]): A sequence (e.g., list, tuple) of
    any type of elements.

    Returns:
    Union[Any, None]: The first element of the sequence if
    it is not empty, otherwise None.

    Example:
    >>> safe_first_element([1, 2, 3])
    1
    >>> safe_first_element([])
    None
    """
    if lst:
        return lst[0]
    else:
        return None
