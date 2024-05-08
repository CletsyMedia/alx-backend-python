#!/usr/bin/env python3
"""
Async Comprehension
"""

import asyncio
from typing import List
from random import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous comprehension to collect 10 random numbers using
    async_generator.
    """
    return [i async for i in async_generator()]


if __name__ == "__main__":
    async def main() -> None:
        """
        Asynchronous function to print the result of async_comprehension.
        """
        print(await async_comprehension())

    asyncio.run(main())
