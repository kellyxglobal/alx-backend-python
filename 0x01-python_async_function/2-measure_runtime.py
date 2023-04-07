#!/usr/bin/env python3


import asyncio
import time
from typing import List
from random import uniform
from asyncio import Task


async def wait_random_time(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds and eventually returns it.

    Args:
        max_delay: An integer representing the maximum delay time
            (default is 10 seconds).

    Returns:
        A float representing the amount of time waited for
        (between 0 and max_delay seconds).
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that spawns wait_random_time n times
    with the specified max_delay argument and returns a list of the
    delay times in ascending order.

    Args:
        n: An integer representing the number of times to spawn
            the wait_random_time coroutine.
        max_delay: An integer representing the maximum delay time
            (default is 10 seconds).

    Returns:
        A list of floats representing the amount of time waited for
        (between 0 and max_delay seconds), in ascending order.
    """
    tasks: List[Task[float]] = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random_time(max_delay)))
    results = await asyncio.gather(*tasks)
    return sorted(results)


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
        n: An integer representing the number of times to spawn
            the wait_random_time coroutine.
        max_delay: An integer representing the maximum delay time
            (default is 10 seconds).

    Returns:
        A float representing the average amount of time waited for
        (between 0 and max_delay seconds), in ascending order.
    """
    start_time = time.monotonic()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.monotonic()
    total_time = end_time - start_time
    return total_time / n
