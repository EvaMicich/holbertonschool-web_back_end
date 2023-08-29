#!/usr/bin/env python3
"""
spawns n number of random wait times and returns these wait times
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns n wait sessions"""
    list_of_all_delays = []
    for count in range(n):
        delay = await wait_random(max_delay)
        list_of_all_delays.append(delay)
    return sorted(list_of_all_delays)
