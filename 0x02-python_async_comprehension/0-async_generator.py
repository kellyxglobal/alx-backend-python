#!/usr/bin/env python3


import asyncio
import random


async def async_generator() -> None:
    """
    Coroutine that loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10 using the random module.

    Args:
        None

    Yields:
        float: a random number between 0 and 10.

    Returns:
        None
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
