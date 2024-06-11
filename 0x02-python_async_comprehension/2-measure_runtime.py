#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of executing async_comprehension
    four times in parallel.

    This coroutine uses asyncio.gather to run
    async_comprehension four times concurrently,
    measures the total runtime, and returns it.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()

    return end_time - start_time
