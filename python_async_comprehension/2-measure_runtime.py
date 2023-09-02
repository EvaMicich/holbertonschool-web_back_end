#!/usr/bin/env python3
"""
Measure runtime of async_comprehension executed four times in parallel.
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure runtime of async_comprehension executed four times in parallel.
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time()
    return end_time - start_time
