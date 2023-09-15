#!/usr/bin/env python3
"""
    doc test
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    a function that index
    """
    return ((page * page_size - page_size), (page * page_size))
