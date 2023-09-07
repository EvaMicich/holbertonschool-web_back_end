#!/usr/bin/env python3
"""pagination"""


def index_range(page, page_size):
    """
    takes two integer arguments
    return a tuple containing a start index and an end index
    """
    start = int(page_size * (page - 1))
    end = int(page * page_size)
    result = (start, end)
    return result
