#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- int float
Return: sum
"""

from typing import List, Union

def sum_mixed_list (mxd_lst: List[Union[int, float]]) -> float:
    """_summary_

    Args:
        mxd_lst (List): mixed list 

    Returns:
        sum
    """
    return sum(mxd_lst)
