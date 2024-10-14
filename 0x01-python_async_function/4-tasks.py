#!/usr/bin/env python3
"""
A module to run multiple async tasks concurrently.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns task_wait_random n times with a max_delay.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): Maximum delay passed to each task.

    Returns:
        list[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
