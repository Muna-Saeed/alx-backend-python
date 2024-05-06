#!/usr/bin/env python3
"""
Tasks module
"""
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times.

    Args:
        n (int): Number of times to spawn task_wait_random coroutine.
        max_delay (int): Maximum delay in seconds
        for each task_wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
