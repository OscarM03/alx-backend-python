#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10.

    This coroutine loops 10 times, and in each iteration, it:
    - Asynchronously waits for 1 second using `await asyncio.sleep(1)`
    - Yields a random float between 0 and 10 using `random.uniform(0, 10)`

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
