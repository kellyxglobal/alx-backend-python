#!/usr/bin/env python3


import asyncio
import time
from typing import List

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that spawns task_wait_random n times
    with the specified max_delay argument and returns a list of the
    delay times in ascending order.

    Args:
        n: An integer representing the number of times to spawn
            the task_wait_random coroutine.
        max_delay: An integer representing the maximum delay time
            (default is 10 seconds).

    Returns:
        A list of floats representing the amount of time waited for
        (between 0 and max_delay seconds), in ascending order.
    """
    tasks: List[Task[float]] = []
    for i in range(n):
        tasks.append(asyncio.create_task(task_wait_random(max_delay)))
    results = await asyncio.gather(*tasks)
    return sorted(results)
