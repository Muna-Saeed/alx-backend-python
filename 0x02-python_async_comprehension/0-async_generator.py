#!/usr/bin/env python3
"""
This module defines an asynchronous generator function `async_generator`
that yields random numbers between 0 and 10 with a one-second delay.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10
    with a one-second delay between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
