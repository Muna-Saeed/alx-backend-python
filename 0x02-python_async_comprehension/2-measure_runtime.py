#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `measure_runtime` that
measures the execution time of running `async_comprehension`
four times in parallel.

It imports `async_comprehension` from the previous task.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    An asynchronous coroutine that measures the total runtime of running
    async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
