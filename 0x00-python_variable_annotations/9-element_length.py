#!/usr/bin/env python3
"""
element length, takes a list as an argument
"""


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    let's duck
    """
    return [(i, len(i)) for i in lst]
