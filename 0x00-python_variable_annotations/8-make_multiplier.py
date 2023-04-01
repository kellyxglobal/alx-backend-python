#!/usr/bin/env python3


def make_multiplier(multiplier: float) -> callable:
    """Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): A floating-point number to
        be used as a multiplier.

    Returns:
        callable: A function that takes a float as input and
        returns the product of the float and the multiplier.
    """

    def multiplier_function(x: float) -> float:
        """Multiplies a float by the given multiplier.

        Args:
            x (float): A floating-point number to be multiplied.

        Returns:
            float: The product of the input number and the multiplier.
        """
        return x * multiplier

    return multiplier_function
