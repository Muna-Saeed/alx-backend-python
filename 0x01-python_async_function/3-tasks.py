#!/usr/bin/env python3
"""
Tasks module
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that returns an asyncio.Task.

    Args:
        max_delay (int): Maximum delay in seconds for the wait_random coroutine.

    Returns:
        asyncio.Task: Task representing the execution of the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
