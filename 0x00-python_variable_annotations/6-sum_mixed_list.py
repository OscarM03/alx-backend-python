#!/usr/bin/env python3
"""Complex types- mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Returns the sum of a mixed list"""
    return float(sum(mxd_lst))
