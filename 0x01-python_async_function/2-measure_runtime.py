#!/usr/bin/env python3
"""
Measures the total execution time for wait_n(n, max_delay).
"""
import time
from typing import Callable

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n

if __name__ == "__main__":
    from 1-concurrent_coroutines import wait_n
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
