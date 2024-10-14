#!/usr/bin/env python3
"""
a simple module to run the async_random as a task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    passing the max_delay arg to the wait_random function
    and returnng a task
    """
    return asyncio.create_task(wait_random(max_delay))
