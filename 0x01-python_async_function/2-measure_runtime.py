#!/usr/bin/env python3
"""
Measure runtime module
"""


import asyncio
import random
from typing import List
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay).

    Args:
      n (int): Number of times to spawn wait_random coroutine.
      max_delay (int): Maximum delay in seconds for each wait_random call.

    Returns:
      float: Total execution time for wait_n(n, max_delay) divided by n.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
