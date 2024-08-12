#!/usr/bin/env python3
"""11. More involved type annotations"""
from typing import TypeVar, Mapping, Any, Union


# Define a type variable
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T], key: Any,
        default: Union[T, None] = None
        ) -> Union[T, None]:
    """
    Retrieves the value associated with the given key
    from the dictionary if it exists.
    Returns the default value if the key is not found.

    Parameters:
    dct (Mapping[Any, T]): A dictionary-like object where the key
    is of any type and the value is of type T.
    key (Any): The key to look up in the dictionary.
    default (Union[T, None], optional): The value to return if the
    key is not found. Defaults to None.

    Returns:
    Union[T, None]: The value associated with the key if found,
    otherwise the default value.

    Example:
    >>> safely_get_value({'a': 1, 'b': 2}, 'a')
    1
    >>> safely_get_value({'a': 1, 'b': 2}, 'c', default=0)
    0
    """
    if key in dct:
        return dct[key]
    else:
        return default
