#!/usr/bin/env python3


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the input string k
    and the square of the input
    integer or float v as a float.

    Args:
        k (str): A string key.
        v (Union[int, float]): An integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the
        input string k and the square of
        the input integer or float v as a float.
    """
    return k, float(v ** 2)
