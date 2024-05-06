#!/usr/bin/env python3
"""
Basic async syntax module
"""


import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
