#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a fucntion"""
    def func(x: float) -> float:
        """Multiplies two floats"""
        return x * multiplier
    return func
