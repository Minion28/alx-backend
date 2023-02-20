#!/usr/bin/env python3
"""
function index_range that takes 2 int arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size 2 containing a start index and end index
    """
    start_index = page * page_size - page_size
    end_index = start_index + page_size
    return (start_index, end_index)
