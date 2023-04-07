#!/usr/bin/env python3


# Import the wait_random coroutine from 0-basic_async_syntax.py
from typing import Task
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> Task[float]:
    """Return an asyncio.Task that waits for a random delay between
    0 and max_delay (inclusive and float value) seconds and eventually
    returns it.
    Args:
        max_delay: An integer representing the maximum delay time
        (inclusive).
    Returns:
        An asyncio.Task object representing the coroutine that will
        wait for a random delay and eventually return it.
    """
    # Create a Task object for the wait_random coroutine
    # with the given max_delay
    task = asyncio.create_task(wait_random(max_delay))

    # Return the Task object
    return task
