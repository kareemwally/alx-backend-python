#!/usr/bin/env python3
"""
implementing the wait_random function for many times n
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    the many times we use the `wait_random` (n)
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    results = []
    for delay in asyncio.as_completed(delays):
        result = await delay
        results.append(result)
    return results
