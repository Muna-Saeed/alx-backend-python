#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element
    from the input iterable and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences
                               (e.g., lists, strings). Each item in the
                               iterable should be a sequence for which
                               the length will be determined.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples. Each tuple contains:
                                - A sequence from the input iterable.
                                - An integer representing the length of
                                  the sequence.

    Example:
    >>> element_length(["hello", [1, 2, 3], (4, 5)])
    [('hello', 5), ([1, 2, 3], 3), ((4, 5), 2)]
    """
    return [(i, len(i)) for i in lst]
