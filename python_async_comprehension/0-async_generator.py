#!/usr/bin/env python3
"""Yield random numbers between 0 and 10 after waiting for 1 second."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield random numbers between 0 and 10 after waiting for 1 second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
