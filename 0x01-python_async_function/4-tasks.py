#!/usr/bin/env python3
"""
Function that creates an asyncio.Task for wait_n.
"""
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates an asyncio.Task for wait_n.
    """
    return await asyncio.create_task(wait_n(n, max_delay))


if __name__ == "__main__":
    import asyncio
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
