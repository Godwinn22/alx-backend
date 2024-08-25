#!/usr/bin/env python3
"""
Simple helper function module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This is a function named index_range that takes
    two integer arguments page and page_size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
