#!/usr/bin/env python3
"""
a simple module with a function to generate a random numbee.
from 0:10 async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> int:
    """
    an asyncrounous function to return a random integer between0:10
    """
    res = random.uniform(0, max_delay)
    await asyncio.sleep(res)
    return res
