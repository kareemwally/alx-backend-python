#!/usr/bin/env python3
"""
implementing the wait_random function for many times n
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """
    the many times we use the `wait_random` (n)
    """
    return [await wait_random(max_delay) for _ in range(n)]
