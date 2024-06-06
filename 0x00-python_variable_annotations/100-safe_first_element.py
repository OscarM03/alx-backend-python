#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""

from typing import List, Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck typing"""
    if lst:
        return lst[0]
    else:
        return None
