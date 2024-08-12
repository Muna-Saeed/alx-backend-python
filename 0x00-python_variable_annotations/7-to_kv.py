#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """"to_kv function with type annotations, using the
    Union and Tuple types from the typing module"""
    return (k, float(v ** 2))
