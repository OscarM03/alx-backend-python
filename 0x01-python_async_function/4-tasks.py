#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called wait_n that takes in 2 int arguments n and max_delay.
    Spawna wait_random n times, and returns a list of delays
    """
    delays = []
    for _ in range(n):
        delays.append(await task_wait_random(max_delay))

    return sorted(delays)
