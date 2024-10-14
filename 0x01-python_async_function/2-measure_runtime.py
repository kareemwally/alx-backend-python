#!/usr/bin/env python3
"""
a simple module to measure the time needed for the
`wait_n` function to excute
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    passing the n, max_delay args to the wait_n function
    and measuring time using the `time` module
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time/n
