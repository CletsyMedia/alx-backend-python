#!/usr/bin/env python3
"""
Module for zoom_array function
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """
    Zoom in an array
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
