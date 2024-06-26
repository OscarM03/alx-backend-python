#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called wait_n that takes in 2 int arguments n and max_delay.
    Spawna wait_random n times, and returns a list of delays
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))

    return sorted(delays)
