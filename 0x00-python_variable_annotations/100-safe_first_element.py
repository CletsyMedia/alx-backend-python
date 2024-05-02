#!/usr/bin/env python3
"""
Module for safe_first_element function
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Return the first element of a sequence safely
    """
    if lst:
        return lst[0]
    else:
        return None
