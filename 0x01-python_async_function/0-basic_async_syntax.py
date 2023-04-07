#!/usr/bin/env python3

import asyncio
import random


async def wait_random_time(wait_random: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay
    between 0 and max_delay (inclusive and float value) seconds and
    eventually returns it.

    Args:
        wait_random: An integer representing the maximum delay time
        (default is 10 seconds).

    Returns:
        A float representing the amount of time waited for
        (between 0 and wait_random seconds).
    """

    # Generate a random delay between 0 and wait_random seconds (inclusive)
    delay = random.uniform(0, wait_random - 1)

    # Wait for the specified delay
    await asyncio.sleep(delay)

    # Return the delay that was waited for
    return delay
