#!/usr/bin/env python3
"""Use async comprehension to get a list of random numbers."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Use async comprehension to get a list of random numbers."""
    return [i async for i in async_generator()]
