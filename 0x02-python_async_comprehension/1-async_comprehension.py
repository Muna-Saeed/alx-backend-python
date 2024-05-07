#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `async_comprehension`
that collects 10 random numbers using an async comprehension and returns them.
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous coroutine that uses an async comprehension to collect
    10 random numbers from the async_generator and returns them as a list.
    """
    return [_ async for _ in async_generator()]
