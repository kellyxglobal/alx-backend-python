"""Module for generating random numbers asynchronously."""


import asyncio
from async_generator import async_generator


@async_generator
async def async_randint(a: int, b: int) -> int:
    """Asynchronous generator that yields random integers
    between `a` and `b` inclusive."""
    while True:
        yield random.randint(a, b)


async def async_comprehension() -> List[int]:
    """Asynchronously collect 10 random numbers using
    async comprehensing over async_generator.

    Returns:
        List of 10 random integers.
    """
    rand_nums = [rand async for rand in async_randint(0, 100)][:10]
    return rand_nums
