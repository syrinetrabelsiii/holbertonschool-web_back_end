#!/usr/bin/env python3
"""
     type-annotated function mxd_list
"""
from typing import List

def sum_mixed_list (mxd_lst: List(Union[int, float])) -> float:
    """ returns their sum as a float
    """ 
    return sum(mxd_lst)
