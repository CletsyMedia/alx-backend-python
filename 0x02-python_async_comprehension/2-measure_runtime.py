#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""

import asyncio
from time import perf_counter
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime for executing async_comprehension four times in
    parallel using asyncio.gather.
    """
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()
    return end_time - start_time


if __name__ == "__main__":
    async def main() -> None:
        """
        Asynchronous function to print the total runtime.
        """
        print(await measure_runtime())

    asyncio.run(main())
