#!/usr/bin/env python3

import asyncio
from typing import List
from datetime import datetime


async def measure_runtime() -> float:
    """
    This coroutine measures the total runtime of executing
    the async_comprehension four times in parallel using asyncio.gather

    Returns:
    -------
    float:
        The total runtime in seconds.
    """

    start_time = datetime.now()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end_time = datetime.now()

    total_runtime = (end_time - start_time).total_seconds()
    return total_runtime
