#!/usr/bin/env python3
"""8. Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """the make_multiplier function with type annotations,
    using the Callable type from the typing module."""
    def multiplier_function(value: float) -> float:
        """another function that multiplies a float by the given multiplier."""
        return value * multiplier
    return multiplier_function
