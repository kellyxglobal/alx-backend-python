#!/usr/bin/env python3


def to_str(n: float) -> str:
    """
    Returns the string representation of a given float.

    Args:
    - n: A float number.

    Returns:
    - The string representation of the input float.

    Raises:
    - TypeError: If the input argument is not a float.
    """
    if not isinstance(n, float):
        raise TypeError("Input argument must be a float.")
    return str(n)
